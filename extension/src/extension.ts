import * as vscode from 'vscode';
import * as path from 'path';
import * as fs from 'fs';
import { AboutPanel } from './aboutPanel';

export function activate(context: vscode.ExtensionContext) {
    console.log('AlibreScript extension is now active!');

    // Show welcome screen on first install or update
    // Disabled for pre-release
    // showWelcomeScreenIfNeeded(context);

    // Register commands
    context.subscriptions.push(
        vscode.commands.registerCommand('alibrescript.newScript', () => {
            createNewScript(context);
        })
    );

    context.subscriptions.push(
        vscode.commands.registerCommand('alibrescript.newNotebook', () => {
            createNewNotebook(context);
        })
    );

    context.subscriptions.push(
        vscode.commands.registerCommand('alibrescript.openExample', () => {
            openExample(context);
        })
    );

    context.subscriptions.push(
        vscode.commands.registerCommand('alibrescript.viewDocs', () => {
            vscode.env.openExternal(vscode.Uri.parse('https://help.alibre.com/articles/#!alibre-help-v28/alibre-script-examples'));
        })
    );

    context.subscriptions.push(
        vscode.commands.registerCommand('alibrescript.showAbout', () => {
            AboutPanel.show(context.extensionUri);
        })
    );

    // Configure Python for AlibreScript
    configureWorkspace(context);
}

async function createNewScript(context: vscode.ExtensionContext) {
    const templates = [
        { label: 'Current Part (Type-Safe)', value: 'current-part' },
        { label: 'Get or Create Part', value: 'get-or-create' },
        { label: 'Basic Part', value: 'basic-part' },
        { label: 'Basic Sketch', value: 'basic-sketch' },
        { label: 'Assembly', value: 'assembly' },
        { label: 'User Input Dialog', value: 'user-input' },
        { label: 'Blank Script', value: 'blank' }
    ];

    const selected = await vscode.window.showQuickPick(templates, {
        placeHolder: 'Select a template'
    });

    if (selected) {
        const templatePath = path.join(context.extensionPath, 'templates', `${selected.value}.py`);
        const content = fs.readFileSync(templatePath, 'utf8');

        const doc = await vscode.workspace.openTextDocument({
            content: content,
            language: 'python'
        });

        await vscode.window.showTextDocument(doc);
        vscode.window.showInformationMessage(`Created new ${selected.label} script!`);
    }
}

async function createNewNotebook(context: vscode.ExtensionContext) {
    const notebooks = [
        { label: 'Getting Started', value: 'getting-started' },
        { label: 'Part Creation', value: 'part-creation' },
        { label: 'Sketch Tutorial', value: 'sketch-tutorial' },
        { label: 'Advanced Features', value: 'advanced-features' },
        { label: 'Blank Notebook', value: 'blank' }
    ];

    const selected = await vscode.window.showQuickPick(notebooks, {
        placeHolder: 'Select a notebook template'
    });

    if (selected) {
        const notebookPath = path.join(context.extensionPath, 'notebooks', `${selected.value}.ipynb`);
        const uri = vscode.Uri.file(notebookPath);

        await vscode.commands.executeCommand('vscode.open', uri);
        vscode.window.showInformationMessage(`Opened ${selected.label} notebook!`);
    }
}

async function openExample(context: vscode.ExtensionContext) {
    const examplesDir = path.join(context.extensionPath, 'examples');
    const files = fs.readdirSync(examplesDir).filter(f => f.endsWith('.py'));

    const items = files.map(f => ({
        label: f.replace('.py', '').replace(/-/g, ' '),
        description: f,
        value: f
    }));

    const selected = await vscode.window.showQuickPick(items, {
        placeHolder: 'Select an example to open'
    });

    if (selected) {
        const examplePath = path.join(examplesDir, selected.value);
        const doc = await vscode.workspace.openTextDocument(examplePath);
        await vscode.window.showTextDocument(doc);
    }
}

function configureWorkspace(context: vscode.ExtensionContext) {
    const config = vscode.workspace.getConfiguration('alibrescript');

    if (config.get('enableTypeHints')) {
        // Set up stub path for Pylance/Pyright
        const stubsPath = path.join(context.extensionPath, 'stubs');
        const pythonConfig = vscode.workspace.getConfiguration('python');

        // Get current extraPaths to avoid overwriting
        const currentExtraPaths = pythonConfig.get<string[]>('analysis.extraPaths', []);
        if (!currentExtraPaths.includes(stubsPath)) {
            const newExtraPaths = [...currentExtraPaths, stubsPath];

            // Try workspace configuration first, fall back to global if no workspace
            const target = vscode.workspace.workspaceFolders
                ? vscode.ConfigurationTarget.Workspace
                : vscode.ConfigurationTarget.Global;

            pythonConfig.update('analysis.extraPaths', newExtraPaths, target);
            pythonConfig.update('analysis.typeCheckingMode', 'basic', target);

            console.log(`AlibreScript: Configured Python analysis with stub path: ${stubsPath}`);
        }
    }
}

// Disabled for pre-release
/*
async function showWelcomeScreenIfNeeded(context: vscode.ExtensionContext) {
    const config = vscode.workspace.getConfiguration('alibrescript');
    const showWelcome = config.get('showWelcomeOnStartup', true);

    // Get the current extension version
    const packageJson = JSON.parse(
        fs.readFileSync(path.join(context.extensionPath, 'package.json'), 'utf8')
    );
    const currentVersion = packageJson.version;

    // Get the last shown version
    const lastVersion = context.globalState.get<string>('lastWelcomeVersion');

    // Show welcome if it's a new install or update, and user hasn't disabled it
    if (showWelcome && currentVersion !== lastVersion) {
        // Show the about panel
        AboutPanel.show(context.extensionUri);

        // Save the current version
        await context.globalState.update('lastWelcomeVersion', currentVersion);
    }
}
*/

export function deactivate() {}
