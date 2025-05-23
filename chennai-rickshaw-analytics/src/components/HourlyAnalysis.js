import React from 'react';
import { Row, Col, Card } from 'react-bootstrap';
import {
  BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer,
  LineChart, Line, Brush, ComposedChart
} from 'recharts';

const HourlyAnalysis = ({ data }) => {
  // Format hours for display (e.g., "01:00" for 1 AM)
  const formattedData = data.map(item => ({
    ...item,
    hourFormatted: `${item.hour.toString().padStart(2, '0')}:00`
  }));

  return (
    <div>
      <h2 className="mb-4">Hourly Analysis</h2>
      <p className="text-muted mb-4">
        This section shows how search tries and driver quotes vary by hour of the day,
        helping identify peak hours and times when driver availability may be limited.
      </p>

      <Card className="mb-4">
        <Card.Body>
          <Card.Title>Search Tries and Quotes by Hour</Card.Title>
          <ResponsiveContainer width="100%" height={400}>
            <ComposedChart data={formattedData}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="hourFormatted" />
              <YAxis yAxisId="left" />
              <YAxis yAxisId="right" orientation="right" />
              <Tooltip />
              <Legend />
              <Bar yAxisId="left" dataKey="totalSearches" name="Total Searches" fill="#8884d8" />
              <Bar yAxisId="left" dataKey="quotesReceived" name="Quotes Received" fill="#82ca9d" />
              <Line yAxisId="right" type="monotone" dataKey="conversionRate" name="Conversion Rate (%)" stroke="#ff7300" />
              <Brush dataKey="hourFormatted" height={30} stroke="#8884d8" />
            </ComposedChart>
          </ResponsiveContainer>
        </Card.Body>
      </Card>

      <Row>
        <Col md={6}>
          <Card className="mb-4 h-100">
            <Card.Body>
              <Card.Title>Avg Trip Distance by Hour</Card.Title>
              <ResponsiveContainer width="100%" height={300}>
                <BarChart data={formattedData}>
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis dataKey="hourFormatted" />
                  <YAxis />
                  <Tooltip formatter={(value) => `${value.toFixed(2)} km`} />
                  <Legend />
                  <Bar dataKey="avgDistance" name="Avg Distance (km)" fill="#8884d8" />
                </BarChart>
              </ResponsiveContainer>
            </Card.Body>
          </Card>
        </Col>
        <Col md={6}>
          <Card className="mb-4 h-100">
            <Card.Body>
              <Card.Title>Avg Base Fare by Hour</Card.Title>
              <ResponsiveContainer width="100%" height={300}>
                <BarChart data={formattedData}>
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis dataKey="hourFormatted" />
                  <YAxis />
                  <Tooltip formatter={(value) => `₹${value.toFixed(2)}`} />
                  <Legend />
                  <Bar dataKey="avgBaseFare" name="Avg Base Fare (₹)" fill="#82ca9d" />
                </BarChart>
              </ResponsiveContainer>
            </Card.Body>
          </Card>
        </Col>
      </Row>

      <Row>
        <Col md={6}>
          <Card className="mb-4 h-100">
            <Card.Body>
              <Card.Title>Avg Pickup Distance by Hour</Card.Title>
              <ResponsiveContainer width="100%" height={300}>
                <BarChart data={formattedData}>
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis dataKey="hourFormatted" />
                  <YAxis />
                  <Tooltip formatter={(value) => `${value.toFixed(2)} meters`} />
                  <Legend />
                  <Bar dataKey="avgPickupDistance" name="Avg Pickup Distance (m)" fill="#ff7300" />
                </BarChart>
              </ResponsiveContainer>
            </Card.Body>
          </Card>
        </Col>
        <Col md={6}>
          <Card className="mb-4 h-100">
            <Card.Body>
              <Card.Title>Ride Status by Hour</Card.Title>
              <ResponsiveContainer width="100%" height={300}>
                <BarChart data={formattedData}>
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis dataKey="hourFormatted" />
                  <YAxis />
                  <Tooltip />
                  <Legend />
                  <Bar dataKey="completed" name="Completed" stackId="a" fill="#4CAF50" />
                  <Bar dataKey="cancelled" name="Cancelled" stackId="a" fill="#F44336" />
                  <Bar dataKey="active" name="Active" stackId="a" fill="#2196F3" />
                </BarChart>
              </ResponsiveContainer>
            </Card.Body>
          </Card>
        </Col>
      </Row>
    </div>
  );
};

export default HourlyAnalysis; 