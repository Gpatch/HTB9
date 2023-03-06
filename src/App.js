import React from "react";
import ReactDOM from "react-dom";

import MapChart from "./components/MapChart";

export default function App() {
  return (
    <div>
      <h1>This is a thing that is different</h1>
      <MapChart />
    </div>
  );
}

const rootElement = document.getElementById("root");
ReactDOM.render(<App />, rootElement);
