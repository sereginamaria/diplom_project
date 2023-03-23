const { defineConfig } = require('@vue/cli-service')
const CopyPlugin = require("copy-webpack-plugin");
const path = require("path");

module.exports = defineConfig({
  transpileDependencies: true
})

module.exports = {
  publicPath: '/education_system',  // TODO

  outputDir: path.resolve(__dirname, "../../education_system/"),
  assetsDir: "../education_system/",

  configureWebpack: {
    plugins: [
      new CopyPlugin({
        patterns: [
          {
            from: path.resolve(__dirname, "../backend/"),
            to: path.resolve(__dirname, "../../education_system/backend/"),
          },
        ],
      }),
    ]
  },
}