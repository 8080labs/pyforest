const notebook = require('@jupyterlab/notebook');
const widgets = require('@jupyter-widgets/base');
const package_ = require('../package.json');
const common = require('./common.js');

module.exports = [{
	id: 'pyforest',
	autoStart: true,
	requires: [notebook.INotebookTracker, widgets.IJupyterWidgetRegistry],
	activate: function (app, notebookTracker, widgetRegistry) {
		const widgetExports = common.makeWidget(
			function () { return getFirstCellDoc().text; },
			function (content) { getFirstCellDoc().text = content; }
		);
		
		function getFirstCellDoc() {
			return notebookTracker.currentWidget.model.cells.get(0).value;
		}
		
		widgetRegistry.registerWidget({
			name: 'pyforest',
			version: package_.version,
			exports: widgetExports
		});
	}
}];
