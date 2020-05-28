/**
 Create a panel, and add listeners for panel show/hide events.
 */
try {
    chrome.devtools.panels.create(
        "HackBar",
        "/icons/icon.png",
        "/theme/hackbar-panel.html"
    );
} catch (e) {
}
