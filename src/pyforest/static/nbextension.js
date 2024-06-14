define(['base/js/namespace', './utils'], function (Jupyter, utils) {
	function load_ipython_extension() {
		utils.setup_notebook(Jupyter);
	}

	return {
		load_ipython_extension: load_ipython_extension
	};
});
