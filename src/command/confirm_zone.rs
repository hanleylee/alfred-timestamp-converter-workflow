use crate::keychain::set_password;
use crate::{SERVICE, TIMEZONE_ACCOUNT};

pub fn run_confirm_zone(zone: &str) -> Result<(), Box<dyn std::error::Error>> {
    set_password(SERVICE, TIMEZONE_ACCOUNT, zone)?;
    Ok(())
}
