import React from "react";
import ReactDOM from "react-dom";

import MapChart from "./MapChart";

export default function App() {
  return (
    <div>
      <MapChart />
    </div>
  );
}

const rootElement = document.getElementById("root");
ReactDOM.render(<App />, rootElement);
