import './App.css';
import {
  BrowserRouter,
  Routes,
  Route,
} from "react-router-dom";
import SignupPage from './pages/Signup';
import LoginPage from './pages/Login';
import HomePage from './pages/Homepage';
import SearchPage from './pages/SearchPage';

function App() {
  return (
    <div className="">
    <div className="">
     <BrowserRouter>
        <Routes>
            <Route path="/login" element={<LoginPage/>} />
            <Route path="/" element={<HomePage/>} />
            <Route path="/signup" element={<SignupPage/>} />
            <Route path="/search" element={<SearchPage/>} />
        </Routes>
      </BrowserRouter>
    </div>
  </div>
  );
}

export default App;