import { Route, Routes } from "react-router-dom";
import DatasetList from "./pages/DatasetList";
import ProjectList from "./pages/ProjectList";
import Login from "./pages/Login";

const App = () => {
  return (
    <Routes>
      <Route path="/login" element={<Login />} />
      <Route path="/projects" element={<ProjectList />} />
      <Route path="/datasets" element={<DatasetList />} />
    </Routes>
  );
};

export default App;
