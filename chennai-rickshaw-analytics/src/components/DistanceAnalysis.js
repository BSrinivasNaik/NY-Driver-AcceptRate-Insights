import React from 'react';
import { Row, Col, Card } from 'react-bootstrap';
import {
  BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer,
  LineChart, Line, ComposedChart
} from 'recharts';

const DistanceAnalysis = ({ data }) => {
  return (
    <div>
      <h2 className="mb-4">Distance Analysis</h2>
      <p className="text-muted mb-4">
        This section analyzes how search try to driver quote conversion rates vary based on trip distance.
        Longer trips may have different conversion patterns compared to shorter ones.
      </p>

      <Row>
        <Col>
          <Card className="mb-4">
            <Card.Body>
              <Card.Title>Search Tries and Quotes by Distance Range</Card.Title>
              <ResponsiveContainer width="100%" height={400}>
                <ComposedChart data={data}>
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis dataKey="distanceRange" />
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
        <Col md={6}>
          <Card className="mb-4 h-100">
            <Card.Body>
              <Card.Title>Conversion Rate by Distance Range</Card.Title>
              <ResponsiveContainer width="100%" height={300}>
                <LineChart data={data}>
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis dataKey="distanceRange" />
                  <YAxis />
                  <Tooltip formatter={(value) => `${value.toFixed(2)}%`} />
                  <Legend />
                  <Line type="monotone" dataKey="conversionRate" name="Conversion Rate (%)" stroke="#ff7300" activeDot={{ r: 8 }} />
                </LineChart>
              </ResponsiveContainer>
            </Card.Body>
          </Card>
        </Col>
        <Col md={6}>
          <Card className="mb-4 h-100">
            <Card.Body>
              <Card.Title>Average Fare by Distance Range</Card.Title>
              <ResponsiveContainer width="100%" height={300}>
                <BarChart data={data}>
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis dataKey="distanceRange" />
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

      <Card className="mb-4">
        <Card.Body>
          <Card.Title>Key Insights - Distance Analysis</Card.Title>
          <ul>
            <li>Observe how conversion rates vary for different trip distances</li>
            <li>Identify distance ranges where drivers are more likely to accept rides</li>
            <li>Note the relationship between trip distance and fare amount</li>
            <li>Understand which distance ranges might need incentives to improve conversion</li>
          </ul>
        </Card.Body>
      </Card>
    </div>
  );
};

export default DistanceAnalysis; 