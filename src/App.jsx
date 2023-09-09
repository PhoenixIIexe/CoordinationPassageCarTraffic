import './App.css';

import { Route, Routes } from 'react-router-dom'
import DistributionWagons from './pages/distribution-wagons/DistributionWagons';

function App() {
    return (
        <div className="App">
            <div className="page">
                <Routes>
                    {/* <Route path="/" element={< />} /> */}
                    <Route path="/" element={<DistributionWagons />} />
                </Routes>
            </div>
        </div>
    );
}

export default App;
