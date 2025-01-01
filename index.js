import express from "express";
import bodyParser from "body-parser";
import morgan from "morgan";

const app = express();

app.use(morgan("dev"));
app.use(express.static("public"));
app.use(bodyParser.urlencoded({ extended: true }));

app.get("/", (req, res) => {
    res.render("./index.ejs")
});

app.listen(3000, () => {
  console.log("Server is running on port 3000");
});