//
//  TimestampConverter.swift
//  alfred-timestamp-converter-workflow
//
//  Created by Hanley Lee on 2024/11/29.
//

import Foundation

public struct TimestampConverter {
    let timezone: TimeZone

    public init(timezone: TimeZone) {
        self.timezone = timezone
    }
}

public extension TimestampConverter {
    func convertTimestampToReadableString(ts: TimeInterval) -> String? {

        return nil
    }

    func convertReadbleStringToTimestamp(str: String) -> TimeInterval? {
        return nil
    }
}

extension TimestampConverter {

    /// 获取当前 UTC 时间字符串
    func nowStr() -> String {
        let formatter = ISO8601DateFormatter()
        return formatter.string(from: Date())
    }

    /// 获取当前时间戳
    func nowTs() -> TimeInterval {
        return Date().timeIntervalSince1970
    }

    /// 将字符串转换为数字
    func strToNum(_ s: String) -> Double? {
        if s.isEmpty {
            return nowTs()
        }
        return Double(s)
    }

    /// 格式化时间戳为指定时区的日期字符串
    func formatTimestamp(_ timestamp: TimeInterval, level: Double, timezone: String) -> [String: String]? {
        guard let tz = TimeZone(identifier: timezone) else {
            return nil
        }

        let date = Date(timeIntervalSince1970: timestamp / level)

        let formatter = DateFormatter()
        formatter.timeZone = tz
        formatter.dateFormat = "yyyy-MM-dd HH:mm:ss"
        let localDateTime = formatter.string(from: date)

        formatter.timeZone = TimeZone(abbreviation: "UTC")
        let utcDateTime = formatter.string(from: date)

        formatter.dateFormat = "yyyy-MM-dd"
        let localDate = formatter.string(from: date)
        let utcDate = formatter.string(from: date)

        return [
            "timestamp": "\(Int(timestamp))",
            "localDateTime": localDateTime,
            "localDate": localDate,
            "utcDateTime": utcDateTime,
            "utcDate": utcDate
        ]
    }
}
