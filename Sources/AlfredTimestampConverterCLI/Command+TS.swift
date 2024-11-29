//
//  Command+TS.swift
//  alfred-timestamp-converter-workflow
//
//  Created by Hanley Lee on 2024/11/29.
//


import AlfredWorkflowScriptFilter
import AlfredWorkflowUpdaterCore
import ArgumentParser
import Foundation
import TimestampConverterCore

extension TimestampLevel: ExpressibleByArgument {}

struct TSCommand: ParsableCommand {
    static let configuration = CommandConfiguration(commandName: "ts", abstract: "convert timestamp to readable time", discussion: "")

    @Option(help: ArgumentHelp("The level of timestamp", valueName: "s|ms"))
    var level: TimestampLevel = .second

    @Argument(help: "query timestamp")
    var timestamp: String = "1234567890"

    func run() throws {
//        let args = CommandLine.arguments
//        if args.isEmpty || args[0].trimmingCharacters(in: .whitespaces).isEmpty {
//            print(Utils.formatTimestamp(Utils.nowTs(), level: 1))
//            return
//        }
//
//        let arg0 = args[0]
//        var trimmedTimestamp: String = ""
//        var level: Double = 1
//
//        if arg0 == "ms" {
//            trimmedTimestamp = args.count > 1 ? args[1] : ""
//            level = 1000
//        } else if arg0 == "s" {
//            trimmedTimestamp = args.count > 1 ? args[1] : ""
//        } else {
//            trimmedTimestamp = arg0
//        }
//
//        if let ts = Utils.strToNum(trimmedTimestamp) {
//            print(Utils.formatTimestamp(ts, level: level))
//        } else {
//            print("Invalid timestamp")
//        }
    }
}

extension TSCommand {
}
//func outputForNoTimezone(_ wf: Workflow) {
//    wf.addItem(
//        title: "No timezone set.",
//        subtitle: "Please use setzone to set your default TimeZone.",
//        valid: false,
//        arg: "",
//        icon: "error_icon.png"
//    )
//    wf.sendFeedback()
//}
//
//func outputForError(_ wf: Workflow) {
//    wf.addItem(
//        title: "Please input correct String/TimeStamp",
//        subtitle: "",
//        valid: false,
//        arg: "",
//        icon: "error_icon.png"
//    )
//    wf.sendFeedback()
//}
//
//func mainOutput(_ wf: Workflow, timestamp: String, level: Double) {
//    // 模拟获取密码（时区）
//    let tsTimezone = "Asia/Shanghai"  // 替代 `wf.get_password`
//
//    guard let ts = Utils.strToNum(timestamp) else {
//        outputForError(wf)
//        return
//    }
//
//    guard let formatted = Utils.formatTimestamp(ts, level: level, timezone: tsTimezone) else {
//        outputForNoTimezone(wf)
//        return
//    }
//
//    let menuItems = [
//        ("\(Int(ts))", "Time Stamp"),
//        (formatted["localDateTime"] ?? "", "\(tsTimezone) Date Time"),
//        (formatted["localDate"] ?? "", "\(tsTimezone) Date"),
//        (formatted["utcDateTime"] ?? "", "UTC Date Time"),
//        (formatted["utcDate"] ?? "", "UTC Date")
//    ]
//
//    for item in menuItems {
//        wf.addItem(
//            title: item.0,
//            subtitle: item.1,
//            valid: true,
//            arg: item.0,
//            icon: "resource/ts_icon.png"
//        )
//    }
//
//    wf.sendFeedback()
//}
