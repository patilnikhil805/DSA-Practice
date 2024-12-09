const express = require("express")
const bodyParser = require("body-parser")
const mongoose = require("mongoose")

const app = express()

app.use(bodyParser.urlencoded({
    extended: true
}));

mongoose.connect("mongodb://localhost:27017/gfg-employees",
    { useNewUrlParser: true}
);

const employeeSchema = {
    employee_name: String,
    employee_department: String,
    employee_salary: Number
}

const EmployeeData = mongoose.model(
    "EmployeeData", employeeSchema
);
app.use(express.static("public"));

app.listen(3000, function(){
    console.log("Server started on port 3000");
});


app.get("/employees", async (req, res) => {
    try {
        const foundEmployees = await EmployeeData.find()
        res.send(foundEmployees);
    }   catch (err) {
        res.send(err)
    }
});

app.post("/employees", async (req, res) => {
    try {
        // Create a new employee instance
        const newEmployee = new EmployeeData({
            employee_name: req.body.employee_name,
            employee_department: req.body.employee_department,
            employee_salary: req.body.employee_salary
        });

        // Saving the employee asynchronously
        await newEmployee.save();

        // Sending a success response
        res.send("Successfully added a new employee.");
    } catch (err) {
        // Sending the error response if something goes wrong
        res.send(err);
    }
});
