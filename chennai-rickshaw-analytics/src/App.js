import React, { useState, useEffect } from 'react';
import { Container, Row, Col, Card, Nav, Navbar, Alert } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';

// Import our components
import HourlyAnalysis from './components/HourlyAnalysis';
import DistanceAnalysis from './components/DistanceAnalysis';
import FareAnalysis from './components/FareAnalysis';
import PickupDistanceAnalysis from './components/PickupDistanceAnalysis';
import Summary from './components/Summary';

function App() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [activeTab, setActiveTab] = useState('summary');

  useEffect(() => {
    // Fetch the data from our JSON file
    fetch('/data.json')
      .then(response => {
        if (!response.ok) {
          throw new Error('Failed to fetch data');
        }
        return response.json();
      })
      .then(jsonData => {
        setData(jsonData);
        setLoading(false);
      })
      .catch(err => {
        console.error('Error fetching data:', err);
        setError(err.message);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return (
      <Container className="mt-5 text-center">
        <h2>Loading data...</h2>
        <p>Please wait while we analyze the Chennai auto-rickshaw data.</p>
      </Container>
    );
  }

  if (error) {
    return (
      <Container className="mt-5">
        <Alert variant="danger">
          <Alert.Heading>Error loading data</Alert.Heading>
          <p>{error}</p>
          <p>
            Make sure you've run the Python script to generate the data.json file.
          </p>
        </Alert>
      </Container>
    );
  }

  return (
    <div className="App">
      <Navbar bg="dark" variant="dark" expand="lg">
        <Container>
          <Navbar.Brand href="#home">Chennai Auto-Rickshaw Analytics</Navbar.Brand>
          <Navbar.Toggle aria-controls="basic-navbar-nav" />
          <Navbar.Collapse id="basic-navbar-nav">
            <Nav className="me-auto">
              <Nav.Link 
                href="#summary" 
                active={activeTab === 'summary'}
                onClick={() => setActiveTab('summary')}
              >
                Summary
              </Nav.Link>
              <Nav.Link 
                href="#hourly" 
                active={activeTab === 'hourly'}
                onClick={() => setActiveTab('hourly')}
              >
                By Hour
              </Nav.Link>
              <Nav.Link 
                href="#distance" 
                active={activeTab === 'distance'}
                onClick={() => setActiveTab('distance')}
              >
                By Distance
              </Nav.Link>
              <Nav.Link 
                href="#fare" 
                active={activeTab === 'fare'}
                onClick={() => setActiveTab('fare')}
              >
                By Fare
              </Nav.Link>
              <Nav.Link 
                href="#pickup" 
                active={activeTab === 'pickup'}
                onClick={() => setActiveTab('pickup')}
              >
                By Pickup Distance
              </Nav.Link>
            </Nav>
          </Navbar.Collapse>
        </Container>
      </Navbar>

      <Container className="mt-4">
        <Row>
          <Col>
            <h1 className="mb-4">Search Try to Driver Quote Analysis</h1>
            <p className="text-muted mb-4">
              Analyzing the search try to driver quote conversion in Chennai auto-rickshaw service.
              This dashboard visualizes the conversion rates across different dimensions: hour of day, distance, fare, and pickup distance.
            </p>
          </Col>
        </Row>

        {activeTab === 'summary' && (
          <Summary data={data.summary} />
        )}

        {activeTab === 'hourly' && (
          <HourlyAnalysis data={data.hourlyData} />
        )}

        {activeTab === 'distance' && (
          <DistanceAnalysis data={data.distanceData} />
        )}

        {activeTab === 'fare' && (
          <FareAnalysis data={data.fareData} />
        )}

        {activeTab === 'pickup' && (
          <PickupDistanceAnalysis data={data.pickupDistanceData} />
        )}
      </Container>

      <footer className="bg-light mt-5 py-3 text-center">
        <p className="text-muted">
          Chennai Auto-Rickshaw Analytics Dashboard &copy; {new Date().getFullYear()}
        </p>
      </footer>
    </div>
  );
}

export default App;
