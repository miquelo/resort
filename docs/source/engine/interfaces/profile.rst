Profile
=======

Component layout.

.. class:: Profile

   Specific layout of components.
   
   .. function:: prepare(props)

      Prepare profile and yields its properties as ( name, value ) tuples.
      
      :param dict props:
         Dictionary with previous properties.

   .. function:: dependencies(comp_name)
   
      Yields dependency component names of the specified component.
      
      :param string comp_name:
         Name of the specified component.
         
   .. function:: component(comp_name)
   
      Definition of the specified component.
      
      :param string comp_name:
         Name of the specified component.
      :rtype:
         Component
