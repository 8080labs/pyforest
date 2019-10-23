var path = require('path');

module.exports = [
	{
		entry: './static/nbextension.js',
		output: {
			filename: 'extension.js',
			path: path.resolve(__dirname, '..', 'pyforest', 'static'),
			libraryTarget: 'amd'
		},
		externals: [],
	},
	{
		entry: './static/nbextension_impl.js',
		output: {
			filename: 'extension_impl.js',
			path: path.resolve(__dirname, '..', 'pyforest', 'static'),
			libraryTarget: 'amd'
		},
		devtool: 'source-map',
		externals: ['base/js/namespace']
	},
];
