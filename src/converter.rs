use chrono::{DateTime, Local, NaiveDate, NaiveDateTime, TimeZone, Utc};
use chrono_tz::Tz;

use crate::ICON_ERROR;
use crate::ICON_TS;
use crate::keychain::get_password;
use crate::{SERVICE, TIMEZONE_ACCOUNT};

#[derive(Debug, Clone)]
pub struct MenuItem {
    pub title: String,
    pub subtitle: String,
}

pub fn now_ts() -> f64 {
    Utc::now().timestamp() as f64 + Utc::now().timestamp_subsec_nanos() as f64 / 1_000_000_000.0
}

pub fn str_to_num(s: &str) -> Option<f64> {
    let s = s.trim();
    if s.is_empty() {
        return Some(now_ts());
    }
    s.parse::<f64>().ok()
}

/// Parse Alfred `ts` query into (timestamp_string, level).
/// level: 1 = seconds, 1000 = milliseconds.
pub fn parse_ts_query(query: &str) -> (String, f64) {
    let parts: Vec<&str> = query.split_whitespace().collect();
    if parts.is_empty() || parts[0].is_empty() {
        return (String::new(), 1.0);
    }
    match parts[0] {
        "ms" => (parts.get(1).copied().unwrap_or("").to_string(), 1000.0),
        "s" => (parts.get(1).copied().unwrap_or("").to_string(), 1.0),
        other => (other.to_string(), 1.0),
    }
}

/// Parse a free-form date/time string into a Unix timestamp (seconds, local interpretation like Python `time.mktime`).
pub fn parse_time_string(input: &str) -> Option<f64> {
    let input = input.trim();
    if input.is_empty() {
        return Some(now_ts());
    }

    // Prefer dtparse (dateutil-like). Fall back to a few common formats.
    if let Ok((naive, _)) = dtparse::parse(input) {
        return Some(local_naive_to_timestamp(naive));
    }

    let formats = [
        "%Y-%m-%d %H:%M:%S",
        "%Y/%m/%d %H:%M:%S",
        "%Y-%m-%d %H:%M",
        "%Y/%m/%d %H:%M",
        "%Y-%m-%d",
        "%Y/%m/%d",
        "%Y%m%d%H%M%S",
        "%Y%m%d",
    ];
    for fmt in formats {
        if let Ok(ndt) = NaiveDateTime::parse_from_str(input, fmt) {
            return Some(local_naive_to_timestamp(ndt));
        }
        if let Ok(nd) = NaiveDate::parse_from_str(input, fmt) {
            return Some(local_naive_to_timestamp(nd.and_hms_opt(0, 0, 0)?));
        }
    }

    if let Ok(dt) = DateTime::parse_from_rfc3339(input) {
        return Some(dt.timestamp() as f64);
    }

    None
}

fn local_naive_to_timestamp(naive: NaiveDateTime) -> f64 {
    Local.from_local_datetime(&naive).single().map(|dt| dt.timestamp() as f64).unwrap_or_else(|| naive.and_utc().timestamp() as f64)
}

pub fn items_no_timezone() -> Vec<MenuItem> {
    vec![MenuItem {
        title: "No timezone set".into(),
        subtitle: "Please use setzone to set your default TimeZone".into(),
    }]
}

pub fn items_error() -> Vec<MenuItem> {
    vec![MenuItem { title: "Please input correct String/TimeStamp".into(), subtitle: String::new() }]
}

pub fn items_for_timestamp(timestamp: impl AsRef<str>, level: f64) -> Vec<MenuItem> {
    let Some(tz_name) = get_password(SERVICE, TIMEZONE_ACCOUNT) else {
        return items_no_timezone();
    };
    let Some(ts) = str_to_num(timestamp.as_ref()) else {
        return items_error();
    };
    let Ok(tz) = tz_name.parse::<Tz>() else {
        return items_no_timezone();
    };

    let seconds = ts / level;
    let Some(utc) = Utc.timestamp_opt(seconds.floor() as i64, ((seconds.fract()) * 1_000_000_000.0) as u32).single() else {
        return items_error();
    };
    let local = utc.with_timezone(&tz);

    let utc_date_time = utc.format("%Y-%m-%d %H:%M:%S").to_string();
    let utc_date = utc.format("%Y-%m-%d").to_string();
    let local_date_time = local.format("%Y-%m-%d %H:%M:%S").to_string();
    let local_date = local.format("%Y-%m-%d").to_string();
    let ts_title = format!("{}", ts.trunc() as i64);

    vec![
        MenuItem { title: ts_title, subtitle: "Time Stamp".into() },
        MenuItem { title: local_date_time, subtitle: format!("{tz_name} Date Time") },
        MenuItem { title: local_date, subtitle: format!("{tz_name} Date") },
        MenuItem { title: utc_date_time, subtitle: "UTC Date Time".into() },
        MenuItem { title: utc_date, subtitle: "UTC Date".into() },
    ]
}

pub fn icon_for_item(valid: bool) -> &'static str {
    if valid { ICON_TS } else { ICON_ERROR }
}
