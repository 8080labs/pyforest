const utils = require('./utils.js');
const notebook = require('@jupyterlab/notebook');

module.exports = [{
	id: 'pyforest',
	autoStart: true,
	requires: [notebook.INotebookTracker],
	activate: function (app, notebookTracker) {
		utils.setup_lab(notebookTracker);
	}
}];
