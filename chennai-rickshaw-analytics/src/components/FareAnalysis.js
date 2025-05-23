import React from 'react';
import { Row, Col, Card } from 'react-bootstrap';
import {
  BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer,
  LineChart, Line, ComposedChart
} from 'recharts';

const FareAnalysis = ({ data }) => {
  return (
    <div>
      <h2 className="mb-4">Fare Analysis</h2>
      <p className="text-muted mb-4">
        This section analyzes how search try to driver quote conversion rates vary based on fare amount.
        Higher fare rides might attract more driver interest, while lower fare rides might have different acceptance patterns.
      </p>

      <Row>
        <Col>
          <Card className="mb-4">
            <Card.Body>
              <Card.Title>Search Tries and Quotes by Fare Range</Card.Title>
              <ResponsiveContainer width="100%" height={400}>
                <ComposedChart data={data}>
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis dataKey="fareRange" />
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
              <Card.Title>Conversion Rate by Fare Range</Card.Title>
              <ResponsiveContainer width="100%" height={300}>
                <LineChart data={data}>
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis dataKey="fareRange" />
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
          <Card.Title>Key Insights - Fare Analysis</Card.Title>
          <ul>
            <li>Observe how conversion rates vary for different fare amounts</li>
            <li>Identify fare ranges where drivers are more likely to accept rides</li>
            <li>Understand if higher fare rides consistently attract more driver quotes</li>
            <li>Determine if there are "sweet spot" fare ranges with optimal conversion rates</li>
            <li>Identify fare ranges that might need incentives to improve driver acceptance</li>
          </ul>
        </Card.Body>
      </Card>

      <Row>
        <Col>
          <Card className="mb-4">
            <Card.Body>
              <Card.Title>Distribution of Rides by Fare Range</Card.Title>
              <ResponsiveContainer width="100%" height={300}>
                <BarChart data={data}>
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis dataKey="fareRange" />
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

export default FareAnalysis; 