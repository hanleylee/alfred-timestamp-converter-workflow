use std::process::Command;

use regex::Regex;

/// Read a generic password from macOS Keychain via `/usr/bin/security`.
pub fn get_password(service: &str, account: &str) -> Option<String> {
    let output = Command::new("/usr/bin/security")
        .args(["find-generic-password", "-g", "-s", service, "-a", account])
        .output()
        .ok()?;

    // `security -g` prints password to stderr.
    let stderr = String::from_utf8_lossy(&output.stderr);
    let re = Regex::new(r#"password: (?:0x([0-9A-F]+)\s*)?\"(.*)\"$"#).ok()?;
    let caps = re.captures(stderr.trim())?;
    if let Some(hex) = caps.get(1) {
        let hex = hex.as_str();
        let mut bytes = Vec::with_capacity(hex.len() / 2);
        let mut chars = hex.chars();
        while let (Some(a), Some(b)) = (chars.next(), chars.next()) {
            if let Ok(byte) = u8::from_str_radix(&format!("{a}{b}"), 16) {
                bytes.push(byte);
            }
        }
        if let Some(nul) = bytes.iter().position(|&b| b == 0) {
            bytes.truncate(nul);
        }
        String::from_utf8(bytes).ok()
    } else {
        Some(caps.get(2)?.as_str().to_string())
    }
}

/// Create or update a generic password in macOS Keychain.
pub fn set_password(service: &str, account: &str, password: &str) -> Result<(), String> {
    let status = Command::new("/usr/bin/security")
        .args(["add-generic-password", "-U", "-a", account, "-s", service, "-p", password])
        .status()
        .map_err(|e| e.to_string())?;
    if status.success() {
        Ok(())
    } else {
        Err(format!("security exited with status: {status}"))
    }
}
