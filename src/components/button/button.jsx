import React from 'react';
import PropTypes from 'prop-types';
import styled from 'styled-components';

const StyledButton = styled.button`
  background: ${({ theme }) => theme.bg};
  color: ${({ theme }) => theme.fg};
  font-size: 2rem;
  margin: 4px;
  padding: 20px 0;
  border: none;
  border-radius: 50px;
  user-select: none;
  line-height: 2.3rem;

  &:hover {
    cursor: pointer;
    background: ${({ theme }) => theme.bgActive};
    border: 1px solid;
  }

  &:focus {
    outline: none;
    border: 1px solid;
  }
  
  &[disabled] {
    opacity: 0.9;
    cursor: not-allowed;
  }
`;


const Button = ({
  children, onClick, className, disabled, ...attrs
}) => {
  const onClickAction = (event) => disabled ? event.preventDefault() : onClick(event);

  return (
    <StyledButton
      className={className}
      disabled={disabled}
      onClick={onClickAction}
      {...attrs}
    >
      {children}
    </StyledButton>
  );
};

Button.propTypes = {
  children: PropTypes.node,
  onClick: PropTypes.func,
  className: PropTypes.string,
  disabled: PropTypes.bool,
};

Button.defaultProps = {
  children: 'Default button',
  onClick: () => {},
  className: '',
  disabled: false,
};

export default Button;
