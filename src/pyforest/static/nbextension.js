if (window.require) {
	window.require.config({
		map: {
			"*" : {
				"pyforest": "nbextensions/pyforest/extension_impl",
			}
		}
	});
}

// Export the required load_ipython_extension
module.exports = {
	load_ipython_extension: function() {}
};
