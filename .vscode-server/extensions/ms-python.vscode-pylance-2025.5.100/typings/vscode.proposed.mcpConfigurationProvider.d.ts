/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/
declare module 'vscode' {
    // https://github.com/microsoft/vscode/issues/243522

    export class McpStdioServerDefinition {
        label: string;

        cwd?: Uri;
        command: string;
        args: readonly string[];
        env: Record<string, string | number | null>;
        version?: string;

        constructor(
            label: string,
            command: string,
            args?: string[],
            env?: Record<string, string | number | null>,
            version?: string
        );
    }

    export class McpSSEServerDefinition {
        label: string;

        uri: Uri;
        headers: [string, string][] | Record<string, string>;
        version?: string;

        constructor(label: string, uri: Uri, headers?: Record<string, string>, version?: string);
    }

    export type McpServerDefinition = McpStdioServerDefinition | McpSSEServerDefinition;

    export interface McpConfigurationProvider {
        onDidChange?: Event<void>;

        provideMcpServerDefinitions(token: CancellationToken): ProviderResult<McpServerDefinition[]>;
    }

    namespace lm {
        export function registerMcpConfigurationProvider(id: string, provider: McpConfigurationProvider): Disposable;
    }
}
