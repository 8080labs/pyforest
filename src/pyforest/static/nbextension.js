define(['base/js/namespace', './common'], function (Jupyter, common) {
	function load_ipython_extension() {
		common.setup_notebook(Jupyter);
	}
	
	return {
		load_ipython_extension: load_ipython_extension
	};
});
