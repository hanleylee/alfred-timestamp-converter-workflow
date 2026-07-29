mod command;
mod converter;
mod keychain;

use alfred::updater_cli::{UpdateAction, run_default_update};
use clap::{Parser, Subcommand};

use command::{run_confirm_zone, run_set_zone, run_st, run_ts};

const GITHUB_REPO: &str = "hanleylee/alfred-timestamp-converter-workflow";
const WORKFLOW_ASSET_NAME: &str = "Timestamp Converter.alfredworkflow";

const SERVICE: &str = "timestamp_converter";
const TIMEZONE_ACCOUNT: &str = "ts_timezone";
const ICON_TS: &str = "./resource/ts_icon.png";
const ICON_ERROR: &str = "/System/Library/CoreServices/CoreTypes.bundle/Contents/Resources/AlertStopIcon.icns";

#[derive(Parser)]
#[command(name = "alfred-timestamp-converter")]
#[command(about = "Tool used for convert timestamp and readable time string")]
struct Cli {
    #[command(subcommand)]
    command: Commands,
}

#[derive(Subcommand)]
enum Commands {
    /// Convert timestamp to readable time
    Ts {
        /// Query: [ms|s] <timestamp>, empty means now
        #[arg(default_value = "")]
        query: String,
    },
    /// Convert readable time string to timestamp
    St {
        /// Readable time string, empty means now
        #[arg(default_value = "")]
        query: String,
    },
    /// List / filter timezones to set as default
    #[command(name = "set-zone")]
    SetZone {
        /// Filter regex for timezone names
        #[arg(default_value = "")]
        query: String,
    },
    /// Persist selected timezone into Keychain
    #[command(name = "confirm-zone")]
    ConfirmZone {
        /// Timezone identifier, e.g. Asia/Shanghai
        zone: String,
    },
    /// Update workflow
    Update {
        #[command(subcommand)]
        action: UpdateAction,
    },
}

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let cli = Cli::parse();
    match cli.command {
        Commands::Ts { query } => run_ts(&query).await?,
        Commands::St { query } => run_st(&query).await?,
        Commands::SetZone { query } => run_set_zone(&query)?,
        Commands::ConfirmZone { zone } => run_confirm_zone(&zone)?,
        Commands::Update { action } => run_default_update(GITHUB_REPO, WORKFLOW_ASSET_NAME, action).await?,
    }
    Ok(())
}
