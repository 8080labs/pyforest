const Jupyter = require('base/js/namespace');
const common = require('./common.js');

function getFirstCellDoc() {
	return Jupyter.notebook.get_cell(0).code_mirror.getDoc();
}

module.exports = common.makeWidget(
	function () { return getFirstCellDoc().getValue(); },
	function (content) { getFirstCellDoc().setValue(content); }
);
