const common = require('./common.js');
const notebook = require('@jupyterlab/notebook');

module.exports = [{
	id: 'pyforest',
	autoStart: true,
	requires: [notebook.INotebookTracker],
	activate: function (app, notebookTracker) {
		common.setup_lab(notebookTracker);
	}
}];
