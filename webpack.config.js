const path= require("path")
const HtmlWebpackPlugin= require("html-webpack-plugin")

module.exports= {
    mode:"development",
    entry:path.join(__dirname, "/src/index.js"),
    output: {
        filename: "bundle.js"
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
        ]
    },
    plugins:[
        new HtmlWebpackPlugin(
            {
                inject: true,
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