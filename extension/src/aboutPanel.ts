import * as vscode from 'vscode';
import * as path from 'path';

export class AboutPanel {
    public static currentPanel: AboutPanel | undefined;
    private readonly _panel: vscode.WebviewPanel;
    private _disposables: vscode.Disposable[] = [];

    private constructor(panel: vscode.WebviewPanel, extensionUri: vscode.Uri) {
        this._panel = panel;
        this._panel.webview.html = this._getHtmlContent();

        this._panel.onDidDispose(() => this.dispose(), null, this._disposables);

        // Handle messages from the webview
        this._panel.webview.onDidReceiveMessage(
            message => {
                switch (message.command) {
                    case 'openExample':
                        vscode.commands.executeCommand('alibrescript.openExample');
                        return;
                    case 'newScript':
                        vscode.commands.executeCommand('alibrescript.newScript');
                        return;
                    case 'newNotebook':
                        vscode.commands.executeCommand('alibrescript.newNotebook');
                        return;
                    case 'openUrl':
                        vscode.env.openExternal(vscode.Uri.parse(message.url));
                        return;
                }
            },
            null,
            this._disposables
        );
    }

    public static show(extensionUri: vscode.Uri) {
        const column = vscode.window.activeTextEditor
            ? vscode.window.activeTextEditor.viewColumn
            : undefined;

        if (AboutPanel.currentPanel) {
            AboutPanel.currentPanel._panel.reveal(column);
            return;
        }

        const panel = vscode.window.createWebviewPanel(
            'alibrescript.about',
            'AlibreScript - Welcome',
            column || vscode.ViewColumn.One,
            {
                enableScripts: true,
                retainContextWhenHidden: true
            }
        );

        AboutPanel.currentPanel = new AboutPanel(panel, extensionUri);
    }

    public dispose() {
        AboutPanel.currentPanel = undefined;
        this._panel.dispose();
        while (this._disposables.length) {
            const disposable = this._disposables.pop();
            if (disposable) {
                disposable.dispose();
            }
        }
    }

    private _getHtmlContent(): string {
        return `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AlibreScript - Welcome</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            padding: 0;
            margin: 0;
            color: var(--vscode-foreground);
            background-color: var(--vscode-editor-background);
        }

        .container {
            max-width: 900px;
            margin: 0 auto;
            padding: 30px 20px;
        }

        .header {
            text-align: center;
            padding: 40px 20px;
            background: linear-gradient(135deg, var(--vscode-button-background) 0%, var(--vscode-button-hoverBackground) 100%);
            border-radius: 12px;
            margin-bottom: 30px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }

        .header h1 {
            margin: 0 0 10px 0;
            font-size: 2.5em;
            color: var(--vscode-button-foreground);
        }

        .header p {
            margin: 0;
            font-size: 1.2em;
            opacity: 0.9;
            color: var(--vscode-button-foreground);
        }

        .quick-start {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }

        .card {
            background-color: var(--vscode-editor-inactiveSelectionBackground);
            border: 1px solid var(--vscode-panel-border);
            border-radius: 8px;
            padding: 25px;
            transition: transform 0.2s, box-shadow 0.2s;
            cursor: pointer;
        }

        .card:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
            border-color: var(--vscode-button-background);
        }

        .card h3 {
            margin: 0 0 12px 0;
            color: var(--vscode-button-background);
            font-size: 1.3em;
        }

        .card p {
            margin: 0;
            line-height: 1.6;
            opacity: 0.85;
        }

        .card .icon {
            font-size: 2em;
            margin-bottom: 10px;
        }

        .section {
            margin-bottom: 30px;
            padding: 25px;
            background-color: var(--vscode-editor-inactiveSelectionBackground);
            border-radius: 8px;
            border-left: 4px solid var(--vscode-button-background);
        }

        .section h2 {
            margin: 0 0 20px 0;
            color: var(--vscode-button-background);
            border-bottom: 2px solid var(--vscode-panel-border);
            padding-bottom: 10px;
        }

        .links {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
            margin-top: 15px;
        }

        .link-button {
            display: inline-block;
            padding: 12px 20px;
            background-color: var(--vscode-button-background);
            color: var(--vscode-button-foreground);
            text-decoration: none;
            border-radius: 6px;
            text-align: center;
            transition: background-color 0.2s;
            cursor: pointer;
            border: none;
            font-size: 1em;
            font-family: inherit;
        }

        .link-button:hover {
            background-color: var(--vscode-button-hoverBackground);
        }

        .link-button.secondary {
            background-color: var(--vscode-button-secondaryBackground);
            color: var(--vscode-button-secondaryForeground);
        }

        .link-button.secondary:hover {
            background-color: var(--vscode-button-secondaryHoverBackground);
        }

        .features {
            list-style: none;
            padding: 0;
            margin: 15px 0;
        }

        .features li {
            padding: 10px 0 10px 30px;
            position: relative;
            line-height: 1.6;
        }

        .features li:before {
            content: "✓";
            position: absolute;
            left: 0;
            color: var(--vscode-button-background);
            font-weight: bold;
            font-size: 1.2em;
        }

        .stats {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 20px;
            margin-top: 20px;
        }

        .stat {
            text-align: center;
            padding: 20px;
            background-color: var(--vscode-editor-background);
            border-radius: 8px;
            border: 1px solid var(--vscode-panel-border);
        }

        .stat-number {
            font-size: 2.5em;
            font-weight: bold;
            color: var(--vscode-button-background);
            margin: 0;
        }

        .stat-label {
            margin: 5px 0 0 0;
            opacity: 0.8;
            font-size: 0.9em;
        }

        .code-example {
            background-color: var(--vscode-textCodeBlock-background);
            padding: 15px;
            border-radius: 6px;
            border: 1px solid var(--vscode-panel-border);
            margin: 15px 0;
            font-family: 'Consolas', 'Courier New', monospace;
            font-size: 0.95em;
            overflow-x: auto;
        }

        .footer {
            text-align: center;
            padding: 30px 20px;
            opacity: 0.7;
            font-size: 0.9em;
            border-top: 1px solid var(--vscode-panel-border);
            margin-top: 40px;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🚀 Welcome to AlibreScript</h1>
            <p>Full IntelliSense, Type Hints & 45+ Examples for Alibre Design</p>
        </div>

        <div class="quick-start">
            <div class="card" onclick="executeCommand('newScript')">
                <div class="icon">📝</div>
                <h3>New Script</h3>
                <p>Create a new AlibreScript from a template with full autocomplete support</p>
            </div>

            <div class="card" onclick="executeCommand('openExample')">
                <div class="icon">📚</div>
                <h3>Browse Examples</h3>
                <p>Explore 45+ ready-to-use example scripts from basic to advanced</p>
            </div>

            <div class="card" onclick="executeCommand('newNotebook')">
                <div class="icon">📓</div>
                <h3>Start Notebook</h3>
                <p>Learn interactively with Jupyter notebooks and step-by-step tutorials</p>
            </div>
        </div>

        <div class="section">
            <h2>🎯 What You Get</h2>

            <div class="stats">
                <div class="stat">
                    <div class="stat-number">47</div>
                    <div class="stat-label">Type Stubs</div>
                </div>
                <div class="stat">
                    <div class="stat-number">45+</div>
                    <div class="stat-label">Examples</div>
                </div>
                <div class="stat">
                    <div class="stat-number">15+</div>
                    <div class="stat-label">Snippets</div>
                </div>
                <div class="stat">
                    <div class="stat-number">100%</div>
                    <div class="stat-label">API Coverage</div>
                </div>
            </div>

            <ul class="features">
                <li><strong>Full IntelliSense</strong> - Autocomplete for all AlibreScript API methods</li>
                <li><strong>Type Hints</strong> - Parameter types and return values in your IDE</li>
                <li><strong>Hover Documentation</strong> - See method docs without leaving your code</li>
                <li><strong>Code Snippets</strong> - Type <code>alibre-</code> and press Tab for quick code</li>
                <li><strong>Real Examples</strong> - 45+ scripts from basic parts to complex assemblies</li>
                <li><strong>Interactive Learning</strong> - Jupyter notebooks for hands-on practice</li>
            </ul>
        </div>

        <div class="section">
            <h2>⚡ Quick Start Guide</h2>

            <h3>1. Enable Autocomplete (One Line!)</h3>
            <div class="code-example"># Auto-import all AlibreScript classes
from AlibreScript import *</div>
            <p>Add this ONE line at the top of your script to get full autocomplete for all 47 classes!</p>
            <p><strong>Tip:</strong> Type <code>alibre-import</code> and press Tab to insert it automatically.</p>

            <h3>2. Create Your First Script</h3>
            <div class="code-example">MyPart = Part('My First Part')
sketch = MyPart.AddSketch('Sketch', MyPart.XYPlane)
sketch.AddRectangle(0, 0, 50, 30, False)
MyPart.AddExtrudeBoss('Body', sketch, 10, False)</div>

            <h3>3. Get Autocomplete</h3>
            <div class="code-example">MyPart.  <span style="opacity: 0.6;">← Type this and see all methods with docs!</span></div>

            <h3>4. Run in Alibre Design</h3>
            <p>Save your script → Open Alibre Design → Automation → Run Script → Select your file</p>
            <p><small>Note: The import line will error in Alibre (it's for VS Code only) - just ignore it!</small></p>
        </div>

        <div class="section">
            <h2>📖 Resources & Links</h2>

            <h3>Official Alibre Resources</h3>
            <div class="links">
                <button class="link-button" onclick="openUrl('https://help.alibre.com/articles/#!alibre-help-v28/alibre-script-examples')">
                    Official Examples
                </button>
                <button class="link-button" onclick="openUrl('https://www.alibre.com/forum/index.php?forums/alibre-script.78/')">
                    Official Forum
                </button>
                <button class="link-button" onclick="openUrl('https://www.alibre.com/')">
                    Alibre Website
                </button>
            </div>

            <h3 style="margin-top: 25px;">Stephen S. Mitchell Resources</h3>
            <div class="links">
                <button class="link-button secondary" onclick="openUrl('https://github.com/stephensmitchell/alibre-script-documentation')">
                    📚 Script Documentation
                </button>
                <button class="link-button secondary" onclick="openUrl('https://github.com/stephensmitchell/alibre-programming')">
                    💻 Alibre Programming
                </button>
                <button class="link-button secondary" onclick="openUrl('https://github.com/stephensmitchell/alibre-script')">
                    🔧 Alibre Script Repo
                </button>
                <button class="link-button secondary" onclick="executeCommand('openExample')">
                    📂 View Local Examples
                </button>
            </div>
        </div>

        <div class="section">
            <h2>💡 Tips & Tricks</h2>

            <ul class="features">
                <li><strong>Ctrl+Space</strong> - Trigger autocomplete manually</li>
                <li><strong>Ctrl+Shift+P</strong> - Open command palette for AlibreScript commands</li>
                <li><strong>Hover over methods</strong> - See full documentation inline</li>
                <li><strong>Browse examples</strong> - Learn from real-world scripts</li>
                <li><strong>Use snippets</strong> - Type alibre- and see available shortcuts</li>
            </ul>
        </div>

        <div class="section">
            <h2>🎓 Learning Path</h2>

            <h3>Beginners</h3>
            <p>1. Open a notebook: <code>Ctrl+Shift+P</code> → "AlibreScript: New Interactive Notebook"</p>
            <p>2. Choose "Getting Started" and follow along</p>
            <p>3. Experiment with code cells</p>

            <h3>Intermediate</h3>
            <p>1. Browse examples: <code>Ctrl+Shift+P</code> → "AlibreScript: Open Example"</p>
            <p>2. Study examples like "Bolt-Creator" or "Getting-User-Input"</p>
            <p>3. Modify them for your projects</p>

            <h3>Advanced</h3>
            <p>1. Use snippets for rapid development</p>
            <p>2. Leverage full autocomplete with type hints</p>
            <p>3. Create complex assemblies and features</p>
        </div>

        <div class="section">
            <h2>🔧 Available Commands</h2>

            <p>Press <strong>Ctrl+Shift+P</strong> and type "AlibreScript" to see all commands:</p>

            <ul class="features">
                <li><strong>New Script from Template</strong> - Quick start with templates</li>
                <li><strong>Open Example</strong> - Browse 45+ example scripts</li>
                <li><strong>New Interactive Notebook</strong> - Start learning with Jupyter</li>
                <li><strong>View API Documentation</strong> - Official Alibre docs</li>
                <li><strong>About AlibreScript</strong> - Show this welcome screen</li>
            </ul>
        </div>

        <div class="footer">
            <p>Made with ❤️ for the Alibre community</p>
            <p>Not affiliated with Alibre, Inc. | MIT Licensed</p>
        </div>
    </div>

    <script>
        const vscode = acquireVsCodeApi();

        function executeCommand(command) {
            vscode.postMessage({
                command: command
            });
        }

        function openUrl(url) {
            vscode.postMessage({
                command: 'openUrl',
                url: url
            });
        }
    </script>
</body>
</html>`;
    }
}
