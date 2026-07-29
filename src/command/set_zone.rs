use alfred::core::AlfredUtils;
use alfred::script_filter::{Icon, Item, ScriptFilter};
use chrono_tz::TZ_VARIANTS;
use regex::Regex;

use crate::ICON_TS;

pub fn run_set_zone(query: &str) -> Result<(), Box<dyn std::error::Error>> {
    ScriptFilter::reset();

    let query = query.trim();
    let zones: Vec<&str> = if query.is_empty() {
        TZ_VARIANTS.iter().map(|tz| tz.name()).collect()
    } else {
        // Match Python: treat query as case-insensitive regex; if invalid, fall back to literal substring.
        let re = Regex::new(&format!("(?i){query}")).unwrap_or_else(|_| {
            let escaped = regex::escape(query);
            Regex::new(&format!("(?i){escaped}")).expect("escaped regex")
        });
        TZ_VARIANTS.iter().map(|tz| tz.name()).filter(|name| re.is_match(name)).collect()
    };

    for zone in zones {
        ScriptFilter::item(
            Item::new(zone)
                .subtitle(format!("Set '{zone}' as default TimeZone"))
                .arg(zone)
                .icon(Icon::new(ICON_TS, None)),
        );
    }

    AlfredUtils::output(ScriptFilter::output());
    Ok(())
}
