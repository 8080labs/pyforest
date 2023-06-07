const utils = require('./utils.js');
const notebook = require('@jupyterlab/notebook');

module.exports = [{
	id: 'pyforest',
	autoStart: true,
	requires: [notebook.INotebookTracker],
	activate: function (app, notebookTracker) {
		// Need to create NotebookPanel and connect it with NotebookTracker first
		notebookTracker.widgetAdded.connect(async (tracker, notebookPanel) => {
			await notebookPanel.revealed;
			utils.setup_lab(notebookPanel);
		});
	}
}];
