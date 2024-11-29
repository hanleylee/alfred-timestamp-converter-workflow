//
//  Command+ST.swift
//  alfred-timestamp-converter-workflow
//
//  Created by Hanley Lee on 2024/11/29.
//
import ArgumentParser
import TimestampConverterCore

struct STCommand: ParsableCommand {
    static let configuration = CommandConfiguration(commandName: "st", abstract: "convert readable time to timestamp", discussion: "")

//    @Option(help: ArgumentHelp("The level of timestamp", valueName: "s|ms"))
//    var level: TimestampLevel = .second

    @Argument(help: "query readable time string")
    var timeStr: String = "1234567890"

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
