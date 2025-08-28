import React from 'react';

const FormField = ({
  label,
  name,
  type = 'text',
  register,
  error,
  required = false,
  placeholder,
  options = [],
  className = '',
  ...props
}) => {
  const baseInputClasses = `
    mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm 
    focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm
    ${error ? 'border-red-300 focus:ring-red-500 focus:border-red-500' : ''}
  `;

  const renderInput = () => {
    switch (type) {
      case 'select':
        return (
          <select
            {...register(name, { required })}
            className={baseInputClasses}
            {...props}
          >
            <option value="">{placeholder || `Sélectionner ${label.toLowerCase()}`}</option>
            {options.map((option) => (
              <option key={option.value} value={option.value}>
                {option.label}
              </option>
            ))}
          </select>
        );
      
      case 'textarea':
        return (
          <textarea
            {...register(name, { required })}
            placeholder={placeholder}
            className={`${baseInputClasses} resize-none`}
            rows={4}
            {...props}
          />
        );
      
      default:
        return (
          <input
            type={type}
            {...register(name, { required })}
            placeholder={placeholder}
            className={baseInputClasses}
            {...props}
          />
        );
    }
  };

  return (
    <div className={className}>
      <label htmlFor={name} className="block text-sm font-medium text-gray-700">
        {label}
        {required && <span className="text-red-500 ml-1">*</span>}
      </label>
      {renderInput()}
      {error && (
        <p className="mt-1 text-sm text-red-600">
          {error.message || `${label} est requis`}
        </p>
      )}
    </div>
  );
};

export default FormField;