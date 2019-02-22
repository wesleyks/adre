const BundleTracker = require('webpack-bundle-tracker');

module.exports = {
  productionSourceMap: false,
  publicPath: 'http://0.0.0.0:8080/',
  chainWebpack: (config) => {
    config.optimization
      .splitChunks(false);
    config
      .plugin(BundleTracker)
      .use(BundleTracker, [{ filename: 'webpack-stats.json' }]);
  },
};
