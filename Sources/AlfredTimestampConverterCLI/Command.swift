//
//  Command.swift
//  alfred-timestamp-converter-workflow
//
//  Created by Hanley Lee on 2024/11/29.
//


import ArgumentParser

struct Command: ParsableCommand {
    @OptionGroup()
    var options: Options

    static let configuration = CommandConfiguration(
        commandName: "alfred-timestamp-converter",
        abstract: "Tool used for convert timestamp and readable time string",
        discussion: "",
        subcommands: [
            TSCommand.self,
            STCommand.self,
        ]
    )

    func run() throws {
        print("Main command run!")
    }
}

extension Command {
    struct Options: ParsableArguments {
        // MARK: - Package Loading
    }
}
