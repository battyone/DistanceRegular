r"""
Morphisms of Toric Varieties

There are three "obvious" ways to map toric varieties to toric
varieties:

1. Polynomial maps in local coordinates, the usual morphisms in
   algebraic geometry.

2. Polynomial maps in the (global) homogeneous coordinates.

3. Toric morphisms, that is, algebraic morphisms equivariant with
   respect to the torus action on the toric variety.

Both 2 and 3 are special cases of 1, which is just to say that we
always remain within the realm of algebraic geometry. But apart from
that, none is included in one of the other cases. In the examples
below, we will explore some algebraic maps that can or can not be
written as a toric morphism. Often a toric morphism can be written
with polynomial maps in homogeneous coordinates, but sometimes it
cannot.

The toric morphisms are perhaps the most mysterious at the
beginning. Let us quickly review their definition (See Definition
3.3.3 of [CLS]_). Let `\Sigma_1` be a fan in `N_{1,\RR}` and `\Sigma_2` be a
fan in `N_{2,\RR}`. A morphism `\phi: X_{\Sigma_1} \to X_{\Sigma_2}`
of the associated toric varieties is toric if `\phi` maps the maximal
torus `T_{N_1} \subseteq X_{\Sigma_1}` into `T_{N_2} \subseteq
X_{\Sigma_2}` and `\phi|_{T_N}` is a group homomorphism.

The data defining a toric morphism is precisely what defines a fan
morphism (see :mod:`~sage.geometry.fan_morphism`), extending the more
familiar dictionary between toric varieties and fans. Toric geometry
is a functor from the category of fans and fan morphisms to the
category of toric varieties and toric morphisms.

.. note::

    Do not create the toric morphisms (or any morphism of schemes)
    directly from the the ``SchemeMorphism...`` classes. Instead, use the
    :meth:`~sage.schemes.generic.scheme.hom` method common to all
    algebraic schemes to create new homomorphisms.

EXAMPLES:

First, consider the following embedding of `\mathbb{P}^1` into
`\mathbb{P}^2` ::

    sage: P2.<x,y,z> = toric_varieties.P2()
    sage: P1.<u,v> = toric_varieties.P1()
    sage: P1.hom([0,u^2+v^2,u*v], P2)
    Scheme morphism:
      From: 1-d CPR-Fano toric variety covered by 2 affine patches
      To:   2-d CPR-Fano toric variety covered by 3 affine patches
      Defn: Defined on coordinates by sending [u : v] to
            [0 : u^2 + v^2 : u*v]

This is a well-defined morphism of algebraic varieties because
homogeneously rescaled coordinates of a point of `\mathbb{P}^1` map to the same
point in `\mathbb{P}^2` up to its homogeneous rescalings. It is not
equivariant with respect to the torus actions

.. math::

    \CC^\times \times \mathbb{P}^1,
    (\mu,[u:v]) \mapsto [u:\mu v]
    \quad\text{and}\quad
    \left(\CC^\times\right)^2 \times \mathbb{P}^2,
    ((\alpha,\beta),[x:y:z]) \mapsto [x:\alpha y:\beta z]
    ,

hence it is not a toric morphism. Clearly, the problem is that
the map in homogeneous coordinates contains summands that transform
differently under the torus action. However, this is not the only
difficulty. For example, consider ::

    sage: phi = P1.hom([0,u,v], P2);  phi
    Scheme morphism:
      From: 1-d CPR-Fano toric variety covered by 2 affine patches
      To:   2-d CPR-Fano toric variety covered by 3 affine patches
      Defn: Defined on coordinates by sending [u : v] to
            [0 : u : v]

This map is actually the embedding of the
:meth:`~sage.schemes.toric.variety.ToricVariety_field.orbit_closure`
associated to one of the rays of the fan of `\mathbb{P}^2`. Now the
morphism is equivariant with respect to **some** map `\CC^\times \to
(\CC^\times)^2` of the maximal tori of `\mathbb{P}^1` and
`\mathbb{P}^2`. But this map of the maximal tori cannot be the same as
``phi`` defined above. Indeed, the image of ``phi`` completely misses
the maximal torus `T_{\mathbb{P}^2} = \{ [x:y:z] | x\not=0, y\not=0,
z\not=0 \}` of `\mathbb{P}^2`.

Consider instead the following morphism of fans::

    sage: fm = FanMorphism( matrix(ZZ,[[1,0]]), P1.fan(), P2.fan() );  fm
    Fan morphism defined by the matrix
    [1 0]
    Domain fan: Rational polyhedral fan in 1-d lattice N
    Codomain fan: Rational polyhedral fan in 2-d lattice N

which also defines a morphism of toric varieties::

    sage: P1.hom(fm, P2)
    Scheme morphism:
      From: 1-d CPR-Fano toric variety covered by 2 affine patches
      To:   2-d CPR-Fano toric variety covered by 3 affine patches
      Defn: Defined by sending Rational polyhedral fan in 1-d lattice N
            to Rational polyhedral fan in 2-d lattice N.

The fan morphism map is equivalent to the following polynomial map::

    sage: _.as_polynomial_map()
    Scheme morphism:
      From: 1-d CPR-Fano toric variety covered by 2 affine patches
      To:   2-d CPR-Fano toric variety covered by 3 affine patches
      Defn: Defined on coordinates by sending [u : v] to
            [u : v : v]

Finally, here is an example of a fan morphism that cannot be written
using homogeneous polynomials. Consider the blowup `O_{\mathbb{P}^1}(2)
\to \CC^2/\ZZ_2`. In terms of toric data, this blowup is::

    sage: A2_Z2 = toric_varieties.A2_Z2()
    sage: A2_Z2.fan().rays()
    N(1, 0),
    N(1, 2)
    in 2-d lattice N
    sage: O2_P1 = A2_Z2.resolve(new_rays=[(1,1)])
    sage: blowup = O2_P1.hom(identity_matrix(2), A2_Z2)
    sage: blowup.as_polynomial_map()
    Traceback (most recent call last):
    ...
    TypeError: The fan morphism cannot be written in homogeneous polynomials.

If we denote the homogeneous coordinates of `O_{\mathbb{P}^1}(2)` by
`x`, `t`, `y` corresponding to the rays `(1,2)`, `(1,1)`, and `(1,0)`
then the blow-up map is [BB]_:

.. math::

    f: O_{\mathbb{P}^1}(2) \to \CC^2/\ZZ_2, \quad
    (x,t,y) \mapsto \left( x\sqrt{t}, y\sqrt{t} \right)

which requires square roots.

REFERENCES:

.. [BB]
    Gavin Brown, Jaroslaw Buczynski:
    Maps of toric varieties in Cox coordinates,
    http://arxiv.org/abs/1004.4924
"""


#*****************************************************************************
#  Copyright (C) 2011 Volker Braun <vbraun.name@gmail.com>
#  Copyright (C) 2010 Andrey Novoseltsev <novoselt@gmail.com>
#  Copyright (C) 2006 William Stein <wstein@gmail.com>
#  Distributed under the terms of the GNU General Public License (GPL)
#                  http://www.gnu.org/licenses/
#*****************************************************************************

# For now, the scheme morphism base class cannot derive from Morphism
# since this would clash with elliptic curves. So we derive only on
# the toric varieties level from Morphism. See
# https://groups.google.com/d/msg/sage-devel/qF4yU6Vdmao/wQlNrneSmWAJ
from sage.categories.morphism import Morphism

from sage.structure.sequence  import Sequence
from sage.rings.all import ZZ
from sage.misc.all import cached_method
from sage.matrix.constructor import matrix, block_matrix, zero_matrix, identity_matrix
from sage.modules.free_module_element import vector
from sage.geometry.cone import Cone
from sage.geometry.fan import Fan

from sage.schemes.generic.scheme import is_Scheme
from sage.schemes.generic.morphism import (
    is_SchemeMorphism,
    SchemeMorphism, SchemeMorphism_point, SchemeMorphism_polynomial
)
from sage.misc.cachefunc import cached_method


############################################################################
# A points on a toric variety determined by homogeneous coordinates.
class SchemeMorphism_point_toric_field(SchemeMorphism_point, Morphism):
    """
    A point of a toric variety determined by homogeneous coordinates
    in a field.

    .. WARNING::

        You should not create objects of this class directly. Use the
        :meth:`~sage.schemes.generic.scheme.hom` method of
        :class:`toric varieties
        <sage.schemes.toric.variety.ToricVariety_field>`
        instead.

    INPUT:

    - ``X`` -- toric variety or subscheme of a toric variety.

    - ``coordinates`` -- list of coordinates in the base field of ``X``.

    - ``check`` -- if ``True`` (default), the input will be checked for
      correctness.

    OUTPUT:

    A :class:`SchemeMorphism_point_toric_field`.

    TESTS::

        sage: fan = FaceFan(lattice_polytope.octahedron(2))
        sage: P1xP1 = ToricVariety(fan)
        sage: P1xP1(1,2,3,4)
        [1 : 2 : 3 : 4]
    """
    # Mimicking affine/projective classes
    def __init__(self, X, coordinates, check=True):
        r"""
        See :class:`SchemeMorphism_point_toric_field` for documentation.

        TESTS::

            sage: fan = FaceFan(lattice_polytope.octahedron(2))
            sage: P1xP1 = ToricVariety(fan)
            sage: P1xP1(1,2,3,4)
            [1 : 2 : 3 : 4]
        """
        # Convert scheme to its set of points over the base ring
        if is_Scheme(X):
            X = X(X.base_ring())
        super(SchemeMorphism_point_toric_field, self).__init__(X)
        if check:
            # Verify that there are the right number of coords
            # Why is it not done in the parent?
            if is_SchemeMorphism(coordinates):
                coordinates = list(coordinates)
            if not isinstance(coordinates, (list, tuple)):
                raise TypeError("coordinates must be a scheme point, list, "
                                "or tuple. Got %s" % coordinates)
            d = X.codomain().ambient_space().ngens()
            if len(coordinates) != d:
                raise ValueError("there must be %d coordinates! Got only %d: "
                                 "%s" % (d, len(coordinates), coordinates))
            # Make sure the coordinates all lie in the appropriate ring
            coordinates = Sequence(coordinates, X.value_ring())
            # Verify that the point satisfies the equations of X.
            X.codomain()._check_satisfies_equations(coordinates)
        self._coords = coordinates



############################################################################
# A morphism of toric varieties determined by homogeneous polynomials.
class SchemeMorphism_polynomial_toric_variety(SchemeMorphism_polynomial, Morphism):
    """
    A morphism determined by homogeneous polynomials.

    .. WARNING::

        You should not create objects of this class directly. Use the
        :meth:`~sage.schemes.generic.scheme.hom` method of
        :class:`toric varieties
        <sage.schemes.toric.variety.ToricVariety_field>`
        instead.

    INPUT:

    Same as for
    :class:`~sage.schemes.generic.morphism.SchemeMorphism_polynomial`.

    OUPUT:

    A :class:`~sage.schemes.generic.morphism.SchemeMorphism_polynomial_toric_variety`.

    TESTS::

        sage: fan = FaceFan(lattice_polytope.octahedron(2))
        sage: P1xP1 = ToricVariety(fan)
        sage: P1xP1.inject_variables()
        Defining z0, z1, z2, z3
        sage: P1 = P1xP1.subscheme(z0-z2)
        sage: H = P1xP1.Hom(P1)
        sage: import sage.schemes.toric.morphism as MOR
        sage: MOR.SchemeMorphism_polynomial_toric_variety(H, [z0,z1,z0,z3])
        Scheme morphism:
          From: 2-d toric variety covered by 4 affine patches
          To:   Closed subscheme of 2-d toric variety
                covered by 4 affine patches defined by:
          z0 - z2
          Defn: Defined on coordinates by sending
                [z0 : z1 : z2 : z3] to [z0 : z1 : z0 : z3]
    """

    def __init__(self, parent, polynomials, check=True):
        r"""
        See :class:`SchemeMorphism_polynomial_toric_variety` for documentation.

        TESTS::

            sage: fan = FaceFan(lattice_polytope.octahedron(2))
            sage: P1xP1 = ToricVariety(fan)
            sage: P1xP1.inject_variables()
            Defining z0, z1, z2, z3
            sage: P1 = P1xP1.subscheme(z0-z2)
            sage: H = P1xP1.Hom(P1)
            sage: import sage.schemes.toric.morphism as MOR
            sage: MOR.SchemeMorphism_polynomial_toric_variety(H, [z0,z1,z0,z3])
            Scheme morphism:
              From: 2-d toric variety covered by 4 affine patches
              To:   Closed subscheme of 2-d toric variety
                    covered by 4 affine patches defined by:
              z0 - z2
              Defn: Defined on coordinates by sending
                    [z0 : z1 : z2 : z3] to [z0 : z1 : z0 : z3]
        """
        SchemeMorphism_polynomial.__init__(self, parent, polynomials, check)
        if check:
            # Check that defining polynomials are homogeneous (degrees can be
            # different if the target uses weighted coordinates)
            for p in self.defining_polynomials():
                if not self.domain().ambient_space().is_homogeneous(p):
                    raise ValueError("%s is not homogeneous!" % p)

    def as_fan_morphism(self):
        """
        Express the morphism as a map defined by a fan morphism.

        OUTPUT:

        A :class:`SchemeMorphism_polynomial_toric_variety`. Raises a
        ``TypeError`` if the morphism cannot be written in such a way.

        EXAMPLES::

            sage: A1.<z> = toric_varieties.A1()
            sage: P1 = toric_varieties.P1()
            sage: patch = A1.hom([1,z], P1)
            sage: patch.as_fan_morphism()
            Traceback (most recent call last):
            ...
            NotImplementedError: expressing toric morphisms as fan morphisms is
            not implemented yet!
        """
        raise NotImplementedError("expressing toric morphisms as fan "
                                  "morphisms is not implemented yet!")


############################################################################
# The embedding morphism of an orbit closure
class SchemeMorphism_orbit_closure_toric_variety(SchemeMorphism, Morphism):
    """
    The embedding of an orbit closure.

    INPUT:

    - ``parent`` -- the parent homset.

    - ``defining_cone`` -- the defining cone.

    - ``ray_map`` -- a dictionary ``{ambient ray generator: orbit ray
      generator}``. Note that the image of the ambient ray generator
      is not necessarily primitive.

    .. WARNING::

        You should not create objects of this class directly. Use the
        :meth:`~sage.schemes.toric.variety.ToricVariety_field.orbit_closure`
        method of :class:`toric varieties
        <sage.schemes.toric.variety.ToricVariety_field>`
        instead.

    EXAMPLES::

        sage: P1xP1 = toric_varieties.P1xP1()
        sage: H = P1xP1.fan(1)[0]
        sage: V = P1xP1.orbit_closure(H)
        sage: V.embedding_morphism()
        Scheme morphism:
          From: 1-d toric variety covered by 2 affine patches
          To:   2-d CPR-Fano toric variety covered by 4 affine patches
          Defn: Defined by embedding the torus closure associated to the 1-d 
                cone of Rational polyhedral fan in 2-d lattice N.

    TESTS::
    
        sage: V.embedding_morphism()._reverse_ray_map()
        {N(-1): 3, N(1): 2}
        sage: V.embedding_morphism()._defining_cone
        1-d cone of Rational polyhedral fan in 2-d lattice N
    """
    def __init__(self, parent, defining_cone, ray_map):
        """
        The Python constructor.

        EXAMPLES::

            sage: P2 = toric_varieties.P2()
            sage: P1 = P2.orbit_closure(P2.fan(1)[0])
            sage: P1.embedding_morphism()
            Scheme morphism:
              From: 1-d toric variety covered by 2 affine patches
              To:   2-d CPR-Fano toric variety covered by 3 affine patches
              Defn: Defined by embedding the torus closure associated to the 1-d cone 
                    of Rational polyhedral fan in 2-d lattice N.
        """
        SchemeMorphism.__init__(self, parent)
        self._defining_cone = defining_cone
        self._ray_map = ray_map

    def defining_cone(self):
        r"""
        Return the cone corresponding to the torus orbit.
        
        OUTPUT:
        
        A cone of the fan of the ambient toric variety.
        
        EXAMPLES::

            sage: P2 = toric_varieties.P2()
            sage: cone = P2.fan(1)[0]
            sage: P1 = P2.orbit_closure(cone)
            sage: P1.embedding_morphism().defining_cone() 
            1-d cone of Rational polyhedral fan in 2-d lattice N
            sage: _ is cone
            True
        """
        return self._defining_cone

    @cached_method
    def _reverse_ray_map(self):
        """
        Reverse ``self._ray_map``.

        OUTPUT:

        Return a dictionary `{orbit ray generator : preimage ray
        index}`. Note that the orbit ray generator need not be
        primitive. Also, the preimage ray is not necessarily unique.

        EXAMPLES::

            sage: P2_112 = toric_varieties.P2_112()
            sage: P1 = P2_112.orbit_closure(Cone([(1,0)]))
            sage: f = P1.embedding_morphism()
            sage: f._ray_map
            {N(0, 1): (1), N(1, 0): (0), N(-1, -2): (-2)}
            sage: f._reverse_ray_map()
            {N(-2): 2, N(1): 1}
        """
        orbit = self.parent().domain()
        codomain_fan = self.parent().codomain().fan()
        reverse_ray_dict = dict()
        defining_cone_indices = []
        for n1,n2 in self._ray_map.iteritems():
            ray_index = codomain_fan.rays().index(n1)
            if n2.is_zero(): 
                assert ray_index in self._defining_cone.ambient_ray_indices()
                continue
            n2 = orbit.fan().lattice()(n2)
            n2.set_immutable()
            reverse_ray_dict[n2] = ray_index
        return reverse_ray_dict

    def _repr_defn(self):
        """
        Return a string representation of the definition of ``self``.

        OUTPUT:

        String.

        EXAMPLES::

            sage: P2 = toric_varieties.P2()
            sage: V = P2.orbit_closure(P2.fan(1)[0]);  V
            1-d toric variety covered by 2 affine patches
            sage: V.embedding_morphism()._repr_defn()
            'Defined by embedding the torus closure associated to the 1-d cone of 
             Rational polyhedral fan in 2-d lattice N.'
        """
        s  = 'Defined by embedding the torus closure associated to the '
        s += str(self._defining_cone)
        s += '.'
        return s

    def as_polynomial_map(self):
        """
        Express the morphism via homogeneous polynomials.

        OUTPUT:

        A :class:`SchemeMorphism_polynomial_toric_variety`. Raises a
        ``TypeError`` if the morphism cannot be written in terms of
        homogeneous polynomials.

        The defining polynomials are not necessarily unique. There are
        choices if multiple ambient space ray generators project to
        the same orbit ray generator, and one such choice is made
        implicitly. The orbit embedding can be written as a polynomial
        map if and only if each primitive orbit ray generator is the
        image of at least one primitive ray generator of the ambient
        toric variety.
        
        EXAMPLES::

            sage: P2 = toric_varieties.P2()
            sage: V = P2.orbit_closure(P2.fan(1)[0]);  V
            1-d toric variety covered by 2 affine patches
            sage: V.embedding_morphism().as_polynomial_map()
            Scheme morphism:
              From: 1-d toric variety covered by 2 affine patches
              To:   2-d CPR-Fano toric variety covered by 3 affine patches
              Defn: Defined on coordinates by sending [z0 : z1] to
                    [0 : z1 : z0]

        If the toric variety is singular, then some orbit closure
        embeddings cannot be written with homogeneous polynomials::

            sage: P2_112 = toric_varieties.P2_112()
            sage: P1 = P2_112.orbit_closure(Cone([(1,0)]))
            sage: P1.embedding_morphism().as_polynomial_map()
            Traceback (most recent call last):
            ...
            TypeError: The embedding cannot be written with homogeneous polynomials.
        """
        orbit = self.domain()
        codomain_fan = self.codomain().fan()
        R = orbit.coordinate_ring()
        polys = [ R.one() ] * codomain_fan.nrays()
        for i in self._defining_cone.ambient_ray_indices():
            polys[i] = R.zero()
        ray_index_map = self._reverse_ray_map()
        for i, ray in enumerate(orbit.fan().rays()):
            try:
                ray_index = ray_index_map[ray]
            except KeyError:
                raise TypeError('The embedding cannot be written with homogeneous polynomials.')
            polys[ray_index] = R.gen(i)
        return SchemeMorphism_polynomial_toric_variety(self.parent(), polys)
        

############################################################################
# A morphism of toric varieties determined by a fan morphism
class SchemeMorphism_fan_toric_variety(SchemeMorphism, Morphism):
    """
    Construct a morphism determined by a fan morphism

    .. WARNING::

        You should not create objects of this class directly. Use the
        :meth:`~sage.schemes.generic.scheme.hom` method of
        :class:`toric varieties
        <sage.schemes.toric.variety.ToricVariety_field>`
        instead.

    INPUT:

    - ``parent`` -- Hom-set whose domain and codomain are toric varieties.

    - ``fan_morphism`` -- A morphism of fans whose domain and codomain
      fans equal the fans of the domain and codomain in the ``parent``
      Hom-set.

    - ``check`` -- boolean (optional, default:``True``). Whether to
      check the input for consistency.

    OUPUT:

    A :class:`~sage.schemes.generic.morphism.SchemeMorphism_fan_toric_variety`.

    EXAMPLES::

        sage: P2 = toric_varieties.P2()
        sage: dP8 = toric_varieties.dP8()
        sage: f = dP8.hom(identity_matrix(2), P2);  f
        Scheme morphism:
          From: 2-d CPR-Fano toric variety covered by 4 affine patches
          To:   2-d CPR-Fano toric variety covered by 3 affine patches
          Defn: Defined by sending Rational polyhedral fan in 2-d lattice N
                to Rational polyhedral fan in 2-d lattice N.
        sage: type(f)
        <class 'sage.schemes.toric.morphism.SchemeMorphism_fan_toric_variety'>

    Slightly more explicit construction::

        sage: P1xP1 = toric_varieties.P1xP1()
        sage: P1 = toric_varieties.P1()
        sage: hom_set = P1xP1.Hom(P1)
        sage: fm = FanMorphism( matrix(ZZ,[[1],[0]]), P1xP1.fan(), P1.fan() )
        sage: hom_set(fm)
        Scheme morphism:
          From: 2-d CPR-Fano toric variety covered by 4 affine patches
          To:   1-d CPR-Fano toric variety covered by 2 affine patches
          Defn: Defined by sending Rational polyhedral fan in 2-d lattice N
               to Rational polyhedral fan in 1-d lattice N.

        sage: P1xP1.hom(fm, P1)
        Scheme morphism:
          From: 2-d CPR-Fano toric variety covered by 4 affine patches
          To:   1-d CPR-Fano toric variety covered by 2 affine patches
          Defn: Defined by sending Rational polyhedral fan in 2-d lattice N
                to Rational polyhedral fan in 1-d lattice N.
    """

    def __init__(self, parent, fan_morphism, check=True):
        r"""
        See :class:`SchemeMorphism_polynomial_toric_variety` for documentation.

        TESTS::

            sage: P1xP1 = toric_varieties.P1xP1()
            sage: P1 = toric_varieties.P1()
            sage: hom_set = P1xP1.Hom(P1)
            sage: fan_morphism = FanMorphism( matrix(ZZ,[[1],[0]]), P1xP1.fan(), P1.fan() )
            sage: from sage.schemes.toric.morphism import SchemeMorphism_fan_toric_variety
            sage: SchemeMorphism_fan_toric_variety(hom_set, fan_morphism)
            Scheme morphism:
              From: 2-d CPR-Fano toric variety covered by 4 affine patches
              To:   1-d CPR-Fano toric variety covered by 2 affine patches
              Defn: Defined by sending Rational polyhedral fan in 2-d lattice N
                    to Rational polyhedral fan in 1-d lattice N.
        """
        SchemeMorphism.__init__(self, parent)
        if check and self.domain().fan()!=fan_morphism.domain_fan():
            raise ValueError('The fan morphism domain must be the fan of the domain.')
        if check and self.codomain().fan()!=fan_morphism.codomain_fan():
            raise ValueError('The fan morphism codomain must be the fan of the codomain.')
        self._fan_morphism = fan_morphism

    def __cmp__(self, right):
        r"""
        Compare ``self`` and ``right``.

        INPUT:

        - ``right`` -- anything.

        OUTPUT:

        - 0 if ``right`` is also a toric morphism between the same domain and
          codomain, given by an equal fan morphism. 1 or -1 otherwise.

        TESTS::

            sage: A2 = toric_varieties.A2()
            sage: P3 = toric_varieties.P(3)
            sage: m = matrix([(2,0,0), (1,1,0)])
            sage: phi = A2.hom(m, P3)
            sage: cmp(phi, phi)
            0
            sage: cmp(phi, prod(phi.factor()))
            0
            sage: cmp(phi, phi.factor()[0])
            -1
            sage: cmp(phi, 1) * cmp(1, phi)
            -1
        """
        if isinstance(right, SchemeMorphism_fan_toric_variety):
            return cmp(
                [self.domain(), self.codomain(), self.fan_morphism()],
                [right.domain(), right.codomain(), right.fan_morphism()])
        else:
            return cmp(type(self), type(right))

    def _composition_(self, right, homset):
        """
        Return the composition of ``self`` and ``right``.

        INPUT:

        - ``right`` -- a toric morphism defined by a fan morphism.

        OUTPUT:

        - a toric morphism.

        EXAMPLES::

            sage: A2 = toric_varieties.A2()
            sage: P3 = toric_varieties.P(3)
            sage: m = matrix([(2,0,0), (1,1,0)])
            sage: phi = A2.hom(m, P3)
            sage: phi1, phi2, phi3 = phi.factor()
            sage: phi1 * phi2
            Scheme morphism:
              From: 2-d affine toric variety
              To:   3-d CPR-Fano toric variety covered by 4 affine patches
              Defn: Defined by sending Rational polyhedral fan in Sublattice
                    <N(1, 0, 0), N(0, 1, 0)> to Rational polyhedral fan in 3-d lattice N.
            sage: phi1 * phi2 * phi3 == phi
            True
        """
        f = self.fan_morphism() * right.fan_morphism()
        return homset(f, self.codomain())

    def _repr_defn(self):
        """
        Return a string representation of the definition of ``self``.

        OUTPUT:

        String.

        EXAMPLES::

            sage: P1xP1 = toric_varieties.P1xP1()
            sage: P1 = toric_varieties.P1()
            sage: f = P1xP1.hom(matrix([[1],[0]]), P1)
            sage: f._repr_defn()
            'Defined by sending Rational polyhedral fan in 2-d lattice N to Rational polyhedral fan in 1-d lattice N.'
        """
        s  = 'Defined by sending '
        s += str(self.domain().fan())
        s += ' to '
        s += str(self.codomain().fan())
        s += '.'
        return s

    def factor(self):
        r"""
        Factor ``self`` into injective * birational * surjective morphisms.

        OUTPUT:

        - a triple of toric morphisms `(\phi_i, \phi_b, \phi_s)`, such that
          `\phi_s` is surjective, `\phi_b` is birational, `\phi_i` is injective,
          and ``self`` is equal to `\phi_i \circ \phi_b \circ \phi_s`.

        The intermediate varieties are universal in the following sense. Let
        ``self`` map `X` to `X'` and let `X_s`, `X_i` seat in between, i.e.

        .. math::

            X
            \twoheadrightarrow
            X_s
            \to
            X_i
            \hookrightarrow
            X'.

        Then any toric morphism from `X` coinciding with ``self`` on the maximal
        torus factors through `X_s` and any toric morphism into `X'` coinciding
        with ``self`` on the maximal torus factors through `X_i`. In particular,
        `X_i` is the closure of the image of ``self`` in `X'`.

        See
        :meth:`~sage.geometry.fan_morphism.FanMorphism.factor`
        for a description of the toric algorithm.

        EXAMPLES:

        We map an affine plane into a projective 3-space in such a way, that it
        becomes "a double cover of a chart of the blow up of one of the
        coordinate planes"::

            sage: A2 = toric_varieties.A2()
            sage: P3 = toric_varieties.P(3)
            sage: m = matrix([(2,0,0), (1,1,0)])
            sage: phi = A2.hom(m, P3)
            sage: phi.as_polynomial_map()
            Scheme morphism:
              From: 2-d affine toric variety
              To:   3-d CPR-Fano toric variety covered by 4 affine patches
              Defn: Defined on coordinates by sending [x : y] to
                    [x^2*y : y : 1 : 1]

            sage: phi.is_surjective(), phi.is_birational(), phi.is_injective()
            (False, False, False)
            sage: phi_i, phi_b, phi_s = phi.factor()
            sage: phi_s.is_surjective(), phi_b.is_birational(), phi_i.is_injective()
            (True, True, True)
            sage: prod(phi.factor()) == phi
            True

        Double cover (surjective)::

            sage: phi_s.as_polynomial_map()
            Scheme morphism:
              From: 2-d affine toric variety
              To:   2-d affine toric variety
              Defn: Defined on coordinates by sending [x : y] to
                    [x^2 : y]

        Blowup chart (birational)::

            sage: phi_b.as_polynomial_map()
            Scheme morphism:
              From: 2-d affine toric variety
              To:   2-d toric variety covered by 3 affine patches
              Defn: Defined on coordinates by sending [z0 : z1] to
                    [z0*z1 : z1 : 1]

        Coordinate plane inclusion (injective)::

            sage: phi_i.as_polynomial_map()
            Scheme morphism:
              From: 2-d toric variety covered by 3 affine patches
              To:   3-d CPR-Fano toric variety covered by 4 affine patches
              Defn: Defined on coordinates by sending [z0 : z1 : z2] to
                    [z0 : z1 : z2 : z2]
        """
        phi_i, phi_b, phi_s = self.fan_morphism().factor()
        from sage.schemes.toric.all import ToricVariety
        X = self.domain()
        X_s = ToricVariety(phi_s.codomain_fan())
        X_i = ToricVariety(phi_i.domain_fan())
        X_prime = self.codomain()
        return X_i.hom(phi_i, X_prime), X_s.hom(phi_b, X_i), X.hom(phi_s, X_s)

    def fan_morphism(self):
        """
        Return the defining fan morphism.

        OUTPUT:

        A :class:`~sage.geometry.fan_morphism.FanMorphism`.

        EXAMPLES::

            sage: P1xP1 = toric_varieties.P1xP1()
            sage: P1 = toric_varieties.P1()
            sage: f = P1xP1.hom(matrix([[1],[0]]), P1)
            sage: f.fan_morphism()
            Fan morphism defined by the matrix
            [1]
            [0]
            Domain fan: Rational polyhedral fan in 2-d lattice N
            Codomain fan: Rational polyhedral fan in 1-d lattice N
        """
        return self._fan_morphism

    def as_polynomial_map(self):
        """
        Express the morphism via homogeneous polynomials.

        OUTPUT:

        A :class:`SchemeMorphism_polynomial_toric_variety`. Raises a
        ``TypeError`` if the morphism cannot be written in terms of
        homogeneous polynomials.

        EXAMPLES::

            sage: A1 = toric_varieties.A1()
            sage: square = A1.hom(matrix([[2]]), A1)
            sage: square.as_polynomial_map()
            Scheme endomorphism of 1-d affine toric variety
              Defn: Defined on coordinates by sending [z] to
                    [z^2]

            sage: P1 = toric_varieties.P1()
            sage: patch = A1.hom(matrix([[1]]), P1)
            sage: patch.as_polynomial_map()
            Scheme morphism:
              From: 1-d affine toric variety
              To:   1-d CPR-Fano toric variety covered by 2 affine patches
              Defn: Defined on coordinates by sending [z] to
                    [z : 1]
        """
        R = self.domain().coordinate_ring()
        phi = self.fan_morphism()
        polys = [R.one()] * phi.codomain_fan().nrays()
        for rho, x in zip(phi.domain_fan(1), R.gens()):
            ray = rho.ray(0)
            sigma = phi.image_cone(rho)
            degrees = sigma.rays().matrix().solve_left(phi(ray))
            for i, d in zip(sigma.ambient_ray_indices(), degrees):
                try:
                    d = ZZ(d)
                except TypeError:
                    raise TypeError('The fan morphism cannot be written in homogeneous polynomials.')
                polys[i] *= x**d
        return SchemeMorphism_polynomial_toric_variety(self.parent(), polys)

    def is_bundle(self):
        r"""
        Check if ``self`` is a bundle.

        See :meth:`~sage.geometry.fan_morphism.FanMorphism.is_bundle`
        for details.

        OUTPUT:

        - ``True`` if ``self`` is a bundle, ``False`` otherwise.

        EXAMPLES::

            sage: P1xP1 = toric_varieties.P1xP1()
            sage: P1 = toric_varieties.P1()
            sage: P1xP1.hom(matrix([[1],[0]]), P1).is_bundle()
            True
        """
        return self.fan_morphism().is_bundle()

    def is_fibration(self):
        r"""
        Check if ``self`` is a fibration.

        See
        :meth:`~sage.geometry.fan_morphism.FanMorphism.is_fibration`
        for details.

        OUTPUT:

        - ``True`` if ``self`` is a fibration, ``False`` otherwise.

        EXAMPLES::

            sage: P1xP1 = toric_varieties.P1xP1()
            sage: P1 = toric_varieties.P1()
            sage: P1xP1.hom(matrix([[1],[0]]), P1).is_fibration()
            True
        """
        return self.fan_morphism().is_fibration()

    def is_injective(self):
        r"""
        Check if ``self`` is injective.

        See
        :meth:`~sage.geometry.fan_morphism.FanMorphism.is_injective`
        for details.

        OUTPUT:

        - ``True`` if ``self`` is injective, ``False`` otherwise.

        EXAMPLES::

            sage: P1xP1 = toric_varieties.P1xP1()
            sage: P1 = toric_varieties.P1()
            sage: P1xP1.hom(matrix([[1],[0]]), P1).is_injective()
            False
        """
        return self.fan_morphism().is_injective()

    def is_surjective(self):
        r"""
        Check if ``self`` is surjective.

        See
        :meth:`~sage.geometry.fan_morphism.FanMorphism.is_surjective`
        for details.

        OUTPUT:

        - ``True`` if ``self`` is surjective, ``False`` otherwise.

        EXAMPLES::

            sage: P1xP1 = toric_varieties.P1xP1()
            sage: P1 = toric_varieties.P1()
            sage: P1xP1.hom(matrix([[1],[0]]), P1).is_surjective()
            True
        """
        return self.fan_morphism().is_surjective()

    @cached_method
    def fiber(self):
        """
        Return a connected component of the generic fiber of the
        morphism.

        Note that the fiber of a toric morphism is constant over the
        maximal torus, so it makes sense to talk about the "generic"
        fiber even if the morphism is not surjective. This method
        returns the fiber over the base point with homogeneous
        coordinates `[1:1:\cdots:1]`.

        The embedding of the generic fiber is a toric morphism. By
        contrast, the embedding of the fiber over lower-dimensional
        torus orbits of the codomain is not a toric morphism. Use
        :meth:`fiber_component` for the latter (non-generic) fibers.

        EXAMPLES::

            sage: P1xP1 = toric_varieties.P1xP1()
            sage: P1 = toric_varieties.P1()
            sage: fiber = P1xP1.hom(matrix([[1],[0]]), P1).fiber()
            sage: fiber
            1-d toric variety covered by 2 affine patches
            sage: f = fiber.embedding_morphism();  f
            Scheme morphism:
              From: 1-d toric variety covered by 2 affine patches
              To:   2-d CPR-Fano toric variety covered by 4 affine patches
              Defn: Defined by sending Rational polyhedral fan in 1-d lattice N to
                    Rational polyhedral fan in 2-d lattice N.
            sage: f.as_polynomial_map()
            Scheme morphism:
              From: 1-d toric variety covered by 2 affine patches
              To:   2-d CPR-Fano toric variety covered by 4 affine patches
              Defn: Defined on coordinates by sending [z0 : z1] to
                    [1 : 1 : z0 : z1]

            sage: A1 = toric_varieties.A1()
            sage: fan = Fan([(0,1,2)], [(1,1,0),(1,0,1),(1,-1,-1)]).subdivide(new_rays=[(1,0,0)])
            sage: f = ToricVariety(fan).hom(matrix([[1],[0],[0]]), A1)
            sage: f.fiber()
            2-d affine toric variety
            sage: f.fiber().fan().cones()
            ((0-d cone of Rational polyhedral fan in 2-d lattice N,),)
        """
        from sage.schemes.toric.variety import ToricVariety
        from sage.geometry.toric_lattice import ToricLattice
        fm = self.fan_morphism()

        # The ker_fan is in a sublattice which does not work yet;
        # rewrite the fan to use a generic lattice
        ker_fan = fm.kernel_fan()
        K = ker_fan.lattice()
        rays = []
        N = ToricLattice(K.dimension())
        for r in ker_fan.rays():
            ray = N(K.echelon_coordinates(r))
            ray.set_immutable()
            rays.append(ray)
        cones = []
        for c in ker_fan.generating_cones():
            cones.append([ker_fan.rays().index(r) for r in c.rays()])
        fiber_fan = Fan(cones, rays, lattice=N)
        fiber = ToricVariety(fiber_fan)

        from sage.geometry.fan_morphism import FanMorphism
        fan_embedding = FanMorphism(K.echelonized_basis_matrix(), fiber_fan, self.domain().fan())
        homset = fiber.Hom(self.domain())
        embedding = SchemeMorphism_fan_toric_variety(homset, fan_embedding)
        fiber._embedding_morphism = embedding
        return embedding.domain()

    def fiber_component(self, domain_cone):
        r"""
        Return the torus orbit closure in the fiber corresponding to
        ``domain_cone``.

        EXAMPLES::

            sage: polytope = Polyhedron(
            ...       [(-3,0,-1,-1),(-1,2,-1,-1),(0,-1,0,0),(0,0,0,1),(0,0,1,0),
            ...        (0,1,0,0),(0,2,-1,-1),(1,0,0,0),(2,0,-1,-1)])
            sage: coarse_fan = FaceFan(polytope.lattice_polytope())
            sage: P2 = toric_varieties.P2()
            sage: proj24 = matrix([[0,0],[1,0],[0,0],[0,1]])
            sage: fm = FanMorphism(proj24, coarse_fan, P2.fan(), subdivide=True)
            sage: fibration = ToricVariety(fm.domain_fan()).hom(fm, P2)
            sage: primitive_cones = fibration.fan_morphism().primitive_preimage_cones(P2.fan(1)[0])
            sage: primitive_cone = primitive_cones[0]
            sage: fibration.fiber_component(primitive_cone)
            2-d toric variety covered by 4 affine patches

            sage: for primitive_cone in primitive_cones:
            ...       print fibration.fiber_component(primitive_cone)
            2-d toric variety covered by 4 affine patches
            2-d toric variety covered by 3 affine patches
            2-d toric variety covered by 3 affine patches
        """
        if domain_cone.is_trivial():
            return self.fiber()
        embedding = SchemeMorphism_fan_fiber_toric_variety(self.domain(), self.fan_morphism(), domain_cone)
        return embedding.domain()

    @cached_method
    def fiber_dimension(self, codomain_cone):
        r"""
        Return the dimension of the fiber over a particular torus
        orbit in the base.

        EXAMPLES::

            sage: P1xP1 = toric_varieties.P1xP1()
            sage: P1 = toric_varieties.P1()
            sage: f = P1xP1.hom(matrix([[1],[0]]), P1)
            sage: f.fiber_dimension(P1.fan(0)[0])
            1
            sage: f.fiber_dimension(P1.fan(1)[0])
            1
            sage: f.fiber_dimension(P1.fan(1)[1])
            1

        Here is a more complicated example that is not a flat fibration::

            sage: A2_Z2 = toric_varieties.A2_Z2()
            sage: O2_P1 = A2_Z2.resolve(new_rays=[(1,1)])
            sage: blowup = O2_P1.hom(identity_matrix(2), A2_Z2)
            sage: blowup.fiber_dimension(A2_Z2.fan(0)[0])
            0
            sage: blowup.fiber_dimension(A2_Z2.fan(1)[0])
            0
            sage: blowup.fiber_dimension(A2_Z2.fan(2)[0])
            1

        This corresponds to the three different fibers::

            sage: blowup.fiber()
            0-d affine toric variety
            sage: blowup.fiber_component(Cone([(1,0)]))
            0-d affine toric variety
            sage: blowup.fiber_component(Cone([(1,1)]))
            1-d toric variety covered by 2 affine patches
        """
        dim = []
        fm = self.fan_morphism()
        base_dim = codomain_cone.dim()
        for c in fm.primitive_preimage_cones(codomain_cone):
            dim.append(base_dim - c.dim())
        return max(dim) + self.domain().dimension() - self.fan_morphism().matrix().rank()

    def fiber_graph(self, codomain_cone):
        r"""
        Return the fiber over a given torus orbit in the codomain.

        INPUT:

        - ``codomain_cone`` -- a cone `\sigma` of the codomain,
          specifying a torus orbit `O(\sigma)`.

        OUTPUT:

        A graph whose nodes are the irreducible components of the
        fiber. If two irreducible components intersect, the
        corresponding nodes of the graph are joined by an edge.

        EXAMPLES::

            sage: polytope = Polyhedron(
            ...       [(-3,0,-1,-1),(-1,2,-1,-1),(0,-1,0,0),(0,0,0,1),(0,0,1,0),
            ...        (0,1,0,0),(0,2,-1,-1),(1,0,0,0),(2,0,-1,-1)])
            sage: coarse_fan = FaceFan(polytope.lattice_polytope())

            sage: P2 = toric_varieties.P2()
            sage: proj34 = block_matrix(2,1,[zero_matrix(2,2), identity_matrix(2)])
            sage: fm = FanMorphism(proj34, coarse_fan, P2.fan(), subdivide=True)
            sage: fibration = ToricVariety(fm.domain_fan()).hom(fm, P2)

            sage: fibration.fiber_graph( P2.fan(0)[0] )
            Graph on 1 vertex
            sage: for c1 in P2.fan(1):
            ...       fibration.fiber_graph(c1)
            Graph on 1 vertex
            Graph on 1 vertex
            Graph on 4 vertices

            sage: fibration.fiber_graph(P2.fan(1)[2]).get_vertices()
            {0: 2-d toric variety covered by 4 affine patches,
             1: 2-d toric variety covered by 3 affine patches,
             2: 2-d toric variety covered by 3 affine patches,
             3: 2-d toric variety covered by 4 affine patches}

            sage: fibration
            Scheme morphism:
              From: 4-d toric variety covered by 18 affine patches
              To:   2-d CPR-Fano toric variety covered by 3 affine patches
              Defn: Defined by sending Rational polyhedral fan in 4-d lattice N
                    to Rational polyhedral fan in 2-d lattice N.
        """
        fm = self.fan_morphism()
        prim = fm.primitive_preimage_cones(codomain_cone)
        n = len(prim)

        def is_union_in_fan(self, c0, c1):
            c = Cone(c0.rays() + c1.rays(), lattice=c0.lattice())
            return fm.domain_fan().contains(c)
        m = matrix(ZZ, n, n, lambda i,j:is_union_in_fan(self,prim[i], prim[j]))

        for i in range(0,n):
            m[i,i]=0
        from sage.graphs.graph import Graph
        graph = Graph(m, loops=False, multiedges=False)
        for i in range(0,n):
            graph.set_vertex(i, self.fiber_component(prim[i]))
        return graph


############################################################################
# The embedding morphism of an orbit closure
class SchemeMorphism_fan_fiber_toric_variety(SchemeMorphism):
    """
    The embedding of an orbit closure inside the fiber of a a toric
    morphism.

    Note that the embedding map of the fiber of a toric morphism is
    itself not a toric morphism!

    INPUT:

    - ``toric_morphism`` -- a toric morphism. The toric morphism whose
      fiber we are describing.

    - ``defining_cone`` -- a cone of a fan. The primitive preimage
      cones of the fan morphism definine the irreducible components of
      the fiber of a toric morphism.

    - ``check`` -- if ``True`` (default), the input will be checked for
      correctness.

    EXAMPLES::

        sage: polytope = Polyhedron(
        ...       [(-3,0,-1,-1),(-1,2,-1,-1),(0,-1,0,0),(0,0,0,1),(0,0,1,0),
        ...        (0,1,0,0),(0,2,-1,-1),(1,0,0,0),(2,0,-1,-1)])
        sage: coarse_fan = FaceFan(polytope.lattice_polytope())
        sage: P2 = toric_varieties.P2()
        sage: proj24 = matrix([[0,0],[1,0],[0,0],[0,1]])
        sage: fm = FanMorphism(proj24, coarse_fan, P2.fan(), subdivide=True)
        sage: fibration = ToricVariety(fm.domain_fan()).hom(fm, P2)
        sage: primitive_cones = fibration.fan_morphism().primitive_preimage_cones(P2.fan(1)[0])
        sage: primitive_cone = primitive_cones[0]
        sage: fiber_component = fibration.fiber_component(primitive_cone)
        sage: fiber_component
        2-d toric variety covered by 4 affine patches
        sage: fiber_component.embedding_morphism()
        Scheme morphism:
          From: 2-d toric variety covered by 4 affine patches
          To:   4-d toric variety covered by 23 affine patches
          Defn: Defined by embedding the fiber irreducible component defined by the
                primitive preimage cone 1-d cone of Rational polyhedral fan in 4-d lattice N.
        sage: fiber_component.embedding_morphism().as_polynomial_map()
        Scheme morphism:
          From: 2-d toric variety covered by 4 affine patches
          To:   4-d toric variety covered by 23 affine patches
          Defn: Defined on coordinates by sending [z0 : z1 : z2 : z3] to
                [1 : 1 : 1 : 1 : z1 : 0 : 1 : z0 : 1 : 1 : 1 : 1 : 1 : z3 : z2]
        sage: type(fiber_component.embedding_morphism())
        <class 'sage.schemes.toric.morphism.SchemeMorphism_fan_fiber_toric_variety'>
    """

    def __init__(self, toric_variety, fan_morphism, defining_cone, check=True):
        """
        The Python constructor.

        TESTS::

            sage: polytope = Polyhedron(
            ...       [(-3,0,-1,-1),(-1,2,-1,-1),(0,-1,0,0),(0,0,0,1),(0,0,1,0),
            ...        (0,1,0,0),(0,2,-1,-1),(1,0,0,0),(2,0,-1,-1)])
            sage: coarse_fan = FaceFan(polytope.lattice_polytope())
            sage: P2 = toric_varieties.P2()
            sage: proj24 = matrix([[0,0],[1,0],[0,0],[0,1]])
            sage: fm = FanMorphism(proj24, coarse_fan, P2.fan(), subdivide=True)
            sage: fibration = ToricVariety(fm.domain_fan()).hom(fm, P2)
            sage: primitive_cone = Cone([(-1, 2, -1, 0)])
            sage: fibration.fiber_component(primitive_cone)
            2-d toric variety covered by 3 affine patches
        """
        if check and toric_variety.fan()!=fan_morphism.domain_fan():
            raise ValueError('The total space toric variety must be the fan morphism codomain.')
        self._fan_morphism = fan_morphism
        self._defining_cone = fan_morphism.domain_fan().embed(defining_cone)
        self._base_cone = fan_morphism.image_cone(defining_cone)
        fiber = self._make_fiber()
        fiber._embedding_morphism = self
        parent = fiber.Hom(toric_variety)
        SchemeMorphism.__init__(self, parent)

    def _repr_defn(self):
        """
        Return a string representation of the definition of ``self``.

        OUTPUT:

        String.

        EXAMPLES::

            sage: P1xP1 = toric_varieties.P1xP1()
            sage: P1 = toric_varieties.P1()
            sage: fiber = P1xP1.hom(matrix([[1],[0]]), P1).fiber_component(Cone([(1,0)]))
            sage: fiber.embedding_morphism()._repr_defn()
            'Defined by embedding the fiber irreducible component defined by the primitive preimage cone 1-d cone of Rational polyhedral fan in 2-d lattice N.'
        """
        s  = 'Defined by embedding the fiber irreducible component defined by the primitive preimage cone '
        s += str(self.defining_cone())
        s += '.'
        return s

    def as_polynomial_map(self):
        """
        Express the embedding morphism via homogeneous polynomials.

        OUTPUT:

        A :class:`SchemeMorphism_polynomial_toric_variety`. Raises a
        ``TypeError`` if the morphism cannot be written in terms of
        homogeneous polynomials.

        EXAMPLES::

            sage: polytope = Polyhedron(
            ...       [(-3,0,-1,-1),(-1,2,-1,-1),(0,-1,0,0),(0,0,0,1),(0,0,1,0),
            ...        (0,1,0,0),(0,2,-1,-1),(1,0,0,0),(2,0,-1,-1)])
            sage: coarse_fan = FaceFan(polytope.lattice_polytope())
            sage: P2 = toric_varieties.P2()
            sage: proj24 = matrix([[0,0],[1,0],[0,0],[0,1]])
            sage: fm = FanMorphism(proj24, coarse_fan, P2.fan(), subdivide=True)
            sage: fibration = ToricVariety(fm.domain_fan()).hom(fm, P2)

            sage: primitive_cone = Cone([(0, 1, 0, 0)])
            sage: f = fibration.fiber_component(primitive_cone).embedding_morphism()
            sage: f.as_polynomial_map()
            Scheme morphism:
              From: 2-d toric variety covered by 4 affine patches
              To:   4-d toric variety covered by 23 affine patches
              Defn: Defined on coordinates by sending [z0 : z1 : z2 : z3] to
                    [1 : 1 : 1 : 1 : z1 : 0 : 1 : z0 : 1 : 1 : 1 : 1 : 1 : z3 : z2]

            sage: primitive_cone = Cone([(-1, 2, -1, 0)])
            sage: f = fibration.fiber_component(primitive_cone).embedding_morphism()
            sage: f.as_polynomial_map()
            Traceback (most recent call last):
            ...
            TypeError: The morphism cannot be written using homogeneous polynomials.
        """
        fiber = self.domain()
        toric_variety = self.codomain()
        R = fiber.coordinate_ring()
        polys = [ R.one() ] * toric_variety.fan().nrays()
        for i in self.defining_cone().ambient_ray_indices():
            polys[i] = R.zero()
        for ray, x in zip(fiber.fan().rays(), R.gens()):
            try:
                ray_index = self._ray_index_map[ray]
            except KeyError:
                raise TypeError('The morphism cannot be written using homogeneous polynomials.')
            polys[ray_index] = x
        return SchemeMorphism_polynomial_toric_variety(self.parent(), polys)

    def _make_fiber(self):
        """
        Construct the fiber component as a toric variety.

        OUTPUT:

        The fiber component as a toric variety.

        EXAMPLES::

            sage: P1xP1 = toric_varieties.P1xP1()
            sage: P1 = toric_varieties.P1()
            sage: fiber = P1xP1.hom(matrix([[1],[0]]), P1).fiber_component(Cone([(1,0)]))
            sage: f = fiber.embedding_morphism()
            sage: f._ray_index_map  # indirect doctest
            {N(-1): 3, N(1): 2}

        TESTS::

            sage: A2_Z2 = toric_varieties.A2_Z2()
            sage: O2_P1 = A2_Z2.resolve(new_rays=[(1,1)])
            sage: blowup = O2_P1.hom(identity_matrix(2), A2_Z2)
            sage: blowup.fiber()
            0-d affine toric variety
            sage: blowup.fiber_component(Cone([(1,0)]))
            0-d affine toric variety
            sage: blowup.fiber_component(Cone([(1,1)]))
            1-d toric variety covered by 2 affine patches
        """
        fm = self._fan_morphism
        defining_cone = self._defining_cone
        base_cone = self._base_cone

        ker = fm.kernel().basis()
        base_cone_preimg = [ fm.matrix().solve_left(r) for r in base_cone.rays() ]
        L = fm.domain_fan().lattice().submodule(ker+base_cone_preimg).saturation()

        cone_L = Cone([L.coordinates(r) for r in defining_cone.rays()])
        L_quotient = cone_L.sublattice_quotient()

        def projection(ray):
            ray_L = L.coordinates(ray)
            return vector(ZZ, L_quotient(ray_L))

        cones = []
        star_rays = set()
        for cone in fm.relative_star_generators(defining_cone):
            star_rays.update(cone.rays())
            projected_rays = [ projection(r) for r in cone.rays() ]
            cones.append(Cone(projected_rays))
        fiber_fan = Fan(cones)

        ray_index_map = dict()
        for ray in star_rays:
            ray_index = fm.domain_fan().rays().index(ray)
            projected_ray = fiber_fan.lattice()(projection(ray))
            if projected_ray.is_zero():
                assert ray in defining_cone.rays()
                continue
            projected_ray.set_immutable()
            ray_index_map[projected_ray] = ray_index
        self._ray_index_map = ray_index_map

        from sage.schemes.toric.variety import ToricVariety
        return ToricVariety(fiber_fan)

    def defining_cone(self):
        r"""
        Return the cone corresponding to the fiber torus orbit.

        OUTPUT:

        A cone of the fan of the total space of the toric fibration.
        """
        return self._defining_cone

    def base_cone(self):
        r"""
        Return the base cone `\sigma`.

        The fiber is constant over the base orbit closure `V(\sigma)`.

        OUTPUT:

        A cone of the base of the toric fibration.
        """
        return self._base_cone
    def is_birational(self):
        r"""
        Check if ``self`` is birational.

        See
        :meth:`~sage.geometry.fan_morphism.FanMorphism.is_birational`
        for a description of the toric algorithm.

        OUTPUT:

        Boolean. Whether ``self`` is birational.

        EXAMPLES::

            sage: X = toric_varieties.A(2)
            sage: Y = ToricVariety(Fan([Cone([(1,0), (1,1)])]))
            sage: m = identity_matrix(2)
            sage: f = Y.hom(m, X)
            sage: f.is_birational()
            True
        """
        return self.fan_morphism().is_birational()

    def is_injective(self):
        r"""
        Check if ``self`` is injective.

        See
        :meth:`~sage.geometry.fan_morphism.FanMorphism.is_injective`
        for a description of the toric algorithm.

        OUTPUT:

        Boolean. Whether ``self`` is injective.

        EXAMPLES::

            sage: X = toric_varieties.A(2)
            sage: m = identity_matrix(2)
            sage: f = X.hom(m, X)
            sage: f.is_injective()
            True

            sage: Y = ToricVariety(Fan([Cone([(1,0), (1,1)])]))
            sage: f = Y.hom(m, X)
            sage: f.is_injective()
            False
        """
        return self.fan_morphism().is_injective()

    def is_surjective(self):
        r"""
        Check if ``self`` is surjective.

        See
        :meth:`~sage.geometry.fan_morphism.FanMorphism.is_surjective`
        for a description of the toric algorithm.

        OUTPUT:

        Boolean. Whether ``self`` is surjective.

        EXAMPLES::

            sage: X = toric_varieties.A(2)
            sage: m = identity_matrix(2)
            sage: f = X.hom(m, X)
            sage: f.is_surjective()
            True

            sage: Y = ToricVariety(Fan([Cone([(1,0), (1,1)])]))
            sage: f = Y.hom(m, X)
            sage: f.is_surjective()
            False
        """
        return self.fan_morphism().is_surjective()
