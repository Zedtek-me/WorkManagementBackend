const path= require("path")
const HtmlWebpackPlugin= require("html-webpack-plugin")

module.exports= {
    mode:"development",
    entry: path.join(__dirname, "/src/index.js"),
    output: {
        // path: path.join(__dirname, "public/"),
        filename: "index_bundle.js"
    },
    module:{
        rules:[
            {
                test: /\.(js|jsx)$/,
                exclude:path.join(__dirname, "node_modules"),
                use:{
                    loader: "babel-loader",
                    options:{
                        presets:["@babel/preset-env", "@babel/preset-react"]
                    }
                }
            },

            {
                test: /\.(css|scss)$/,
                use: {
                    loader:"css-loader"
                }
            }
        ]
    },
    plugins:[
        new HtmlWebpackPlugin(
            {
                inject: "body",
                template: path.join(__dirname, "public/index.html")
            }
        )
    ],

    devServer:{
        //configs for the webpack-dev-server
        static: {
            directory: path.join(__dirname, "public")
        },
        hot:true,

        port: 9000,
        compress:true,
        
    }
}