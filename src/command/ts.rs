use alfred::core::AlfredUtils;
use alfred::script_filter::{Icon, Item, ScriptFilter};

use crate::command::update_check::{check_for_update_silently, maybe_append_update_item};
use crate::converter::{icon_for_item, items_for_timestamp, parse_ts_query};

pub async fn run_ts(query: &str) -> Result<(), Box<dyn std::error::Error>> {
    ScriptFilter::reset();

    let (trimmed, level) = parse_ts_query(query);
    let items = if trimmed.is_empty() {
        items_for_timestamp("", level)
    } else {
        items_for_timestamp(&trimmed, level)
    };

    let valid = items.first().is_some_and(|i| i.subtitle == "Time Stamp");
    for item in &items {
        let mut sf_item = Item::new(&item.title).subtitle(&item.subtitle).valid(valid).icon(Icon::new(icon_for_item(valid), None));
        if valid {
            sf_item = sf_item.arg(&item.title);
        }
        ScriptFilter::item(sf_item);
    }

    let need_check = maybe_append_update_item().await;
    AlfredUtils::output(ScriptFilter::output());
    if need_check {
        check_for_update_silently();
    }
    Ok(())
}
