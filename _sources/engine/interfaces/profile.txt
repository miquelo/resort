Profile
=======

Component layout.

.. class:: Profile

   Specific layout of components.
   
   .. function:: prepare(props)

      Prepare profile return its properties.
      
      :param dict props:
         Dictionary with previous properties.
      :rtype:
         dict
      :return:
         Properties dictionary.
         
   .. function:: dependencies(comp_name)
   
      Yields dependency component names of the specified component.
      
      :param str comp_name:
         Name of the specified component.
         
   .. function:: component(comp_name)
   
      Definition of the specified component.
      
      :param str comp_name:
         Name of the specified component.
      :rtype:
         Component
