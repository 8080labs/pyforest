define([], function () {
	function setup_lab(notebookTracker) {
		window.update_imports_cell = function (importStr) {
			var cv = notebookTracker.currentWidget.model.cells.get(0).value;
			cv.text = updateImports(importStr, cv.text);
		};
	}
	
	function setup_notebook(Jupyter) {
		window.update_imports_cell = function (importStr) {
			var doc = Jupyter.notebook.get_cell(0).code_mirror.getDoc();
			doc.setValue(updateImports(importStr, doc.getValue()));
		};
	}
	
	function updateImports(importStr, currentContent) {
		var sep = '# ^^^ pyforest imports ^^^';
		var parts = currentContent.split(sep);
		if (parts.length > 1) {
			parts = parts.splice(1);
		}
		return importStr + '\n' + sep + '\n' + parts.join('\n').trim('\n');
	}
	
	return {
		setup_lab: setup_lab,
		setup_notebook: setup_notebook
	};
});
