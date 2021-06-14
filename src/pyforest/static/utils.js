define([], function () {
	function first_code_cell_in_lab(notebookPanel) {
		var cells = notebookPanel.content.widgets
		for (let index in cells) {
			if (cells[index].model.type == "code") {
				return index;
			}
      	}
		// This should never happen because this function is called when the user
		// executes a code cell.
		throw new Error("No single code cell found");
	}

	function setup_lab(notebookPanel) {
		window._pyforest_update_imports_cell = function (imports_string) {
			var first_code_cell_index = first_code_cell_in_lab(notebookPanel)
			var cell = notebookPanel.model.cells.get(first_code_cell_index).value;
			cell.text = get_new_cell_content(imports_string, cell.text);
		};
	}

	function first_code_cell_in_notebook(Jupyter) {
		var cells = Jupyter.notebook.get_cells();
		for (let index in cells) {
			if (cells[index]["cell_type"] == "code") {
				return index;
			}
		}
		// This should never happen because this function is called when the user
		// executes a code cell.
		throw new Error("No single code cell found");
	}

	function setup_notebook(Jupyter) {
		window._pyforest_update_imports_cell = function (imports_string) {
			var first_code_cell_index = first_code_cell_in_notebook(Jupyter)
			var cell_doc = Jupyter.notebook.get_cell(first_code_cell_index).code_mirror.getDoc();
			cell_doc.setValue(get_new_cell_content(imports_string, cell_doc.getValue()));
		};
	}

	function get_new_cell_content(imports_string, current_content) {
		var separator = `# ^^^ pyforest auto-imports - don't write above this line`;
        var parts = current_content.split(separator);
        var user_content = ""
		if (parts.length > 1) {
            // User content is everything after the first separator.
            // If the user adds another separator, pyforest only updates the content above the first separator.
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
