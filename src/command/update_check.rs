use std::time::Duration;

use alfred::core::AlfredConst;
use alfred::script_filter::{Item, ScriptFilter, Variable};
use alfred::updater::{Updater, version_compare};

use crate::{GITHUB_REPO, WORKFLOW_ASSET_NAME};

/// Append "new version" ScriptFilter item when a newer release is cached.
/// Returns the updater so the caller can run a silent check after ScriptFilter output.
pub async fn maybe_append_update_item() -> Updater {
    let updater = Updater::new(GITHUB_REPO, WORKFLOW_ASSET_NAME, Duration::from_secs(60 * 60 * 24));
    let alfred = AlfredConst::shared();
    if let Some(cached) = updater.read_cached_release().await.ok().and_then(|o| o) {
        if updater.cache_valid(&cached) {
            if let Some(ref current_version) = alfred.workflow_version {
                if version_compare(current_version, &cached.tag_name) == std::cmp::Ordering::Less {
                    ScriptFilter::item(
                        Item::new("New version available on GitHub, type [Enter] to update")
                            .subtitle(format!("current version: {}, remote version: {}", current_version, cached.tag_name))
                            .arg("update")
                            .variable(Variable::new(Some("HAS_UPDATE".into()), Some("1".into()))),
                    );
                }
            }
        }
    }
    updater
}
