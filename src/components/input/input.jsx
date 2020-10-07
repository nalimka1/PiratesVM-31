import React from 'react';
import PropTypes from 'prop-types';
import styled from 'styled-components';

const StyledLabel = styled.label`
  color: white;
  font-size: 1.6rem;
  font-weight: 600;
`;

const StyledInput = styled.input`
  font-size: 2.2rem;
  padding: 20px 8px;
  min-width: 280px;
  margin: 8px;
  color: white;
  background: transparent;
  border: none;
  border-bottom: 2px solid #6fb38e;
  outline: none;
  
  &::placeholder {
    font-size: 2rem;
    color: white;
  }
  
  &:-webkit-autofill,
  &:-webkit-autofill:hover, 
  &:-webkit-autofill:focus, 
  &:-webkit-autofill:active {
    background-color: #6fb38e;
  }
`;

const StyledError = styled.span`
  margin-top: 10px;
  color: whitesmoke;
  font-size: 1.4rem;
`;


const Input = ({
  id, className, label, error, ...attrs
}) => {
  return (
    <>
      {label
        && <StyledLabel htmlFor={id}>{label}</StyledLabel>
      }
      <StyledInput
        name={id}
        id={id}
        className={className}
        {...attrs}
      />
      {error
        && <StyledError>{error}</StyledError>
      }
    </>
  );
};

Input.propTypes = {
  id: PropTypes.string.isRequired,
  className: PropTypes.string,
  label: PropTypes.string,
  error: PropTypes.string,
};

Input.defaultProps = {
  className: '',
  label: '',
  error: '',
};

export default Input;
