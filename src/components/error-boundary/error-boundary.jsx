import React from 'react';
import ErrorIndicator from './error-indicator';

class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false };
  }

  static getDerivedStateFromError(error) {
    return { hasError: true };
  }

  componentDidCatch(error, info) {
    this.setState({
      hasError: true,
    });
  }

  clearError() {
    this.setState({
      hasError: false,
    });
  }

  render() {
    if (this.state.hasError) {
      return <ErrorIndicator resetError={this.clearError} />;
    }
    return this.props.children;
  }
}

export default ErrorBoundary;
