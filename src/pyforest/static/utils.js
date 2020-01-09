define([], function () {
	function setup_lab(notebookTracker) {
		window._pyforest_update_imports_cell = function (imports_string) {
			var cell = notebookTracker.currentWidget.model.cells.get(0).value;
			cell.text = get_new_cell_content(imports_string, cell.text);
		};
	}

	function setup_notebook(Jupyter) {
		window._pyforest_update_imports_cell = function (imports_string) {
			var cell_doc = Jupyter.notebook.get_cell(0).code_mirror.getDoc();
			cell_doc.setValue(get_new_cell_content(imports_string, cell_doc.getValue()));
		};
	}

	function get_new_cell_content(imports_string, current_content) {
		var separator = `# ^^^ pyforest auto-imports - don't write above this line`;
        var parts = current_content.split(separator);
        var user_content = ""
		if (parts.length > 1) {
            // user content is everything after the first separator
            // if the user adds another separator, pyforest only updates the content above the first separator
            user_content = parts.slice(1)
		} else {
            user_content = parts
        }
		return imports_string + '\n' + separator + '\n' + user_content.join('\n').trim('\n');
	}

	return {
		setup_lab: setup_lab,
		setup_notebook: setup_notebook
	};
});
