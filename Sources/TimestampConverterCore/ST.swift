//
//  ST.swift
//  alfred-timestamp-converter-workflow
//
//  Created by Hanley Lee on 2024/11/29.
//


import Foundation

//struct ST {
//    static func run(args: [String]) {
//        if args.isEmpty || args[0].trimmingCharacters(in: .whitespaces).isEmpty {
//            print(Utils.formatTimestamp(Utils.nowTs(), level: 1))
//            return
//        }
//
//        let arg0 = args[0]
//        let formatter = DateFormatter()
//        formatter.dateFormat = "yyyy-MM-dd HH:mm:ss"
//
//        if let date = formatter.date(from: arg0) {
//            let timestamp = date.timeIntervalSince1970
//            print(Utils.formatTimestamp(timestamp, level: 1))
//        } else {
//            print("Invalid date string")
//        }
//    }
//}
