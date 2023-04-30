import React, { useState } from "react";
import "./App.css";

function App() {
  const [formData, setFormData] = useState({
    age: "",
    gender: "",
    amount: "",
    category: "",
  });

  const [result, setResult] = useState("");
  const [isDisabled, setIsDisabled] = useState(true);
  const [isLoading, setIsLoading] = useState(false);

  const handleChange = (event) => {
    const { name, value } = event.target;
    setFormData({ ...formData, [name]: value });
  };
  const handleSubmit = (event) => {
    event.preventDefault();
    setIsLoading(true);
    setTimeout(() => {
      setFormData({
        age: "",
        gender: "",
        amount: "",
        category: "",
      });
      setResult(Math.random() < 0.5 ? "Fraud" : "Not fraud");
      setIsDisabled(true);
      setIsLoading(false);
    }, 1500);
  }
  // TODO: Showing the result based on the response of the POST request 
  // const handleSubmit = 
  // async (event) => {
  //   event.preventDefault();
  //   setIsLoading(true);
  //   try {
  //     const response = await fetch("/predict-features", {
  //       method: "POST",
  //       headers: {
  //         "Content-Type": "application/json",
  //       },
  //       body: JSON.stringify(formData),
  //     });
  //     const data = await response.json();
  //     setResult(data.prediction);
  //   } catch (error) {
  //     console.error(error);
  //   } finally {
  //     setIsLoading(false);
  //     setIsDisabled(true);
  //   }
  // };

  const handleInput = () => {
    const isFormFilled = Object.values(formData).every((value) => value !== "");
    setIsDisabled(!isFormFilled);
  };
  return (
    <div>
      <img
        src="https://user-images.githubusercontent.com/79907283/235289093-3e7e958c-9427-448d-b2c5-d7d753394931.png"
        alt="logo"
        className="logo"
      />

      <div className="container">
        <h1 className="title">Fraud Detection</h1>
        <form className="form-input" onSubmit={handleSubmit}>
          <label>
            Age
            <input
              type="number"
              name="age"
              value={formData.age}
              onChange={handleChange}
              onInput={handleInput}
              className="input"
            />
          </label>
          <br />
          <label>
            Gender
            <select
              className="select-input"
              name="gender"
              onChange={handleChange}
              onInput={handleInput}
              value={formData.gender}
            >
              <option value="" disabled selected>
                Select your option
              </option>
              <option >M</option>
              <option>F</option>
            </select>
          </label>
          <br />
          <label>
            Amount
            <input
              type="number"
              name="amount"
              value={formData.amount}
              onChange={handleChange}
              onInput={handleInput}
              className="input"
            />
          </label>
          <br />
          <label>
            Category
            <select
              name="category"
              onChange={handleChange}
              onInput={handleInput}
              value={formData.category}
              className="select-input"
            >
              <option value="" disabled selected>
                Select your option
              </option>
              <option >es_transportation</option>
              <option >es_health</option>
              <option >es_leisure</option>
              <option >es_sportsandtoys</option>
              <option >es_food</option>
              <option >es_home</option>
              <option >es_wellnessandbeauty</option>
            </select>
          </label>
          <br />
          <button type="submit" disabled={isDisabled} className="submit-button">
            {isLoading ? "Loading..." : "Check Fraud"}
          </button>
        </form>
        {isLoading && (
          <img
            src="https://user-images.githubusercontent.com/79907283/235289093-3e7e958c-9427-448d-b2c5-d7d753394931.png"
            alt="logo"
          ></img>
        )}

        {!isLoading && result && (
          <p className={`"result" ${result === "Fraud" ? "result-red" : ""}`}>
            {result}
          </p>
        )}
      </div>
    </div>
  );
}

export default App;
// To do: Sending the form data to our api
// fetch post request

