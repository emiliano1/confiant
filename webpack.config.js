module.exports = {
    entry: "./src/ui/index.jsx",
    module: {
        rules: [{
            test: /\.jsx?$/,
            exclude: /node_modules/,
            use: {
                loader: "babel-loader"
            }
        }]
    },
    resolve: {
        extensions: [".js", ".jsx", ".json"],
    },
    output: {
        filename: "app.js",
        path: __dirname + "/src/public/js"
    },
};
