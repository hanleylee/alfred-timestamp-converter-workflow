use alfred::core::AlfredUtils;
use alfred::script_filter::{Icon, Item, ScriptFilter};

use crate::command::update_check::maybe_append_update_item;
use crate::converter::{icon_for_item, items_for_timestamp, now_ts, parse_time_string};

pub async fn run_st(query: &str) -> Result<(), Box<dyn std::error::Error>> {
    ScriptFilter::reset();

    let items = if query.trim().is_empty() {
        items_for_timestamp(now_ts().to_string(), 1.0)
    } else if let Some(ts) = parse_time_string(query) {
        items_for_timestamp(ts.to_string(), 1.0)
    } else {
        // Match Python: fall back to "now" when parse fails
        items_for_timestamp(now_ts().to_string(), 1.0)
    };

    let valid = items.first().is_some_and(|i| i.subtitle == "Time Stamp");
    for item in &items {
        let mut sf_item = Item::new(&item.title).subtitle(&item.subtitle).valid(valid).icon(Icon::new(icon_for_item(valid), None));
        if valid {
            sf_item = sf_item.arg(&item.title);
        }
        ScriptFilter::item(sf_item);
    }

    let updater = maybe_append_update_item().await;
    AlfredUtils::output(ScriptFilter::output());
    updater.check_for_update_silently_if_stale().await;
    Ok(())
}
