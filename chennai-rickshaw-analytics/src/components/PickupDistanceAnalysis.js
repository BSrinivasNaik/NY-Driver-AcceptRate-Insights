import React from 'react';
import { Row, Col, Card } from 'react-bootstrap';
import {
  BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer,
  LineChart, Line, ComposedChart
} from 'recharts';

const PickupDistanceAnalysis = ({ data }) => {
  // Calculate conversion rate correctly
  const dataWithCorrectConversionRate = data.map(item => ({
    ...item,
    conversionRate: (item.quotesReceived / item.totalSearches) * 100
  }));

  return (
    <div>
      <h2 className="mb-4">Pickup Distance Analysis</h2>
      <p className="text-muted mb-4">
        This section analyzes how search try to driver quote conversion rates vary based on the distance
        to pickup location. Shorter pickup distances may have higher acceptance rates from drivers.
      </p>

      <Row>
        <Col>
          <Card className="mb-4">
            <Card.Body>
              <Card.Title>Search Tries and Quotes by Pickup Distance</Card.Title>
              <ResponsiveContainer width="100%" height={400}>
                <ComposedChart data={dataWithCorrectConversionRate}>
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis dataKey="pickupRange" />
                  <YAxis yAxisId="left" />
                  <YAxis yAxisId="right" orientation="right" />
                  <Tooltip />
                  <Legend />
                  <Bar yAxisId="left" dataKey="totalSearches" name="Total Searches" fill="#8884d8" />
                  <Bar yAxisId="left" dataKey="quotesReceived" name="Quotes Received" fill="#82ca9d" />
                  <Line yAxisId="right" type="monotone" dataKey="conversionRate" name="Conversion Rate (%)" stroke="#ff7300" />
                </ComposedChart>
              </ResponsiveContainer>
            </Card.Body>
          </Card>
        </Col>
      </Row>

      <Row>
        <Col md={12}>
          <Card className="mb-4">
            <Card.Body>
              <Card.Title>Conversion Rate by Pickup Distance</Card.Title>
              <ResponsiveContainer width="100%" height={300}>
                <LineChart data={dataWithCorrectConversionRate}>
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis dataKey="pickupRange" />
                  <YAxis />
                  <Tooltip formatter={(value) => `${value.toFixed(2)}%`} />
                  <Legend />
                  <Line type="monotone" dataKey="conversionRate" name="Conversion Rate (%)" stroke="#ff7300" activeDot={{ r: 8 }} />
                </LineChart>
              </ResponsiveContainer>
            </Card.Body>
          </Card>
        </Col>
      </Row>

      <Card className="mb-4">
        <Card.Body>
          <Card.Title>Key Insights - Pickup Distance Analysis</Card.Title>
          <ul>
            <li>Observe how conversion rates vary based on distance to pickup location</li>
            <li>Identify if there's a threshold distance beyond which driver acceptance drops significantly</li>
            <li>Understand the relationship between pickup distance and quote conversion</li>
            <li>Determine optimal pickup distance ranges for maximizing driver quotes</li>
            <li>Identify pickup distance ranges that might need incentives to improve driver acceptance</li>
          </ul>
        </Card.Body>
      </Card>

      <Row>
        <Col>
          <Card className="mb-4">
            <Card.Body>
              <Card.Title>Distribution of Rides by Pickup Distance</Card.Title>
              <ResponsiveContainer width="100%" height={300}>
                <BarChart data={dataWithCorrectConversionRate}>
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis dataKey="pickupRange" />
                  <YAxis />
                  <Tooltip />
                  <Legend />
                  <Bar dataKey="totalSearches" name="Total Search Tries" fill="#8884d8" />
                </BarChart>
              </ResponsiveContainer>
            </Card.Body>
          </Card>
        </Col>
      </Row>
    </div>
  );
};

export default PickupDistanceAnalysis; 