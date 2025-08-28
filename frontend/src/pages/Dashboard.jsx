import React from 'react';
import { useMyRequests, usePendingRequests } from '../hooks/useRequests';
import { useEmployees } from '../hooks/useEmployees';
import StatusBadge from '../components/StatusBadge';
import LoadingSpinner from '../components/LoadingSpinner';
import {
  ClockIcon,
  UserGroupIcon,
  DocumentTextIcon,
  CheckCircleIcon,
} from '@heroicons/react/outline';

const Dashboard = () => {
  const { data: myRequests, isLoading: loadingMyRequests } = useMyRequests();
  const { data: pendingRequests, isLoading: loadingPending } = usePendingRequests();
  const { data: employees, isLoading: loadingEmployees } = useEmployees();

  const stats = [
    {
      name: 'Mes demandes',
      value: myRequests?.length || 0,
      icon: ClockIcon,
      color: 'bg-blue-500',
      loading: loadingMyRequests,
    },
    {
      name: 'Demandes en attente',
      value: pendingRequests?.length || 0,
      icon: DocumentTextIcon,
      color: 'bg-yellow-500',
      loading: loadingPending,
    },
    {
      name: 'Employés',
      value: employees?.length || 0,
      icon: UserGroupIcon,
      color: 'bg-green-500',
      loading: loadingEmployees,
    },
    {
      name: 'Demandes approuvées',
      value: myRequests?.filter(r => r.status === 'accepted')?.length || 0,
      icon: CheckCircleIcon,
      color: 'bg-purple-500',
      loading: loadingMyRequests,
    },
  ];

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-bold text-gray-900">Tableau de bord</h1>
        <p className="mt-1 text-sm text-gray-500">
          Vue d'ensemble de votre activité
        </p>
      </div>

      {/* Statistiques */}
      <div className="grid grid-cols-1 gap-5 sm:grid-cols-2 lg:grid-cols-4">
        {stats.map((stat) => (
          <div key={stat.name} className="bg-white overflow-hidden shadow rounded-lg">
            <div className="p-5">
              <div className="flex items-center">
                <div className="flex-shrink-0">
                  <div className={`p-3 rounded-md ${stat.color}`}>
                    <stat.icon className="h-6 w-6 text-white" />
                  </div>
                </div>
                <div className="ml-5 w-0 flex-1">
                  <dl>
                    <dt className="text-sm font-medium text-gray-500 truncate">
                      {stat.name}
                    </dt>
                    <dd className="text-lg font-medium text-gray-900">
                      {stat.loading ? <LoadingSpinner size="sm" /> : stat.value}
                    </dd>
                  </dl>
                </div>
              </div>
            </div>
          </div>
        ))}
      </div>

      {/* Mes dernières demandes */}
      <div className="bg-white shadow rounded-lg">
        <div className="px-6 py-4 border-b border-gray-200">
          <h2 className="text-lg font-medium text-gray-900">Mes dernières demandes</h2>
        </div>
        <div className="p-6">
          {loadingMyRequests ? (
            <LoadingSpinner />
          ) : myRequests && myRequests.length > 0 ? (
            <div className="space-y-4">
              {myRequests.slice(0, 5).map((request) => (
                <div key={request.requestID} className="flex items-center justify-between p-4 bg-gray-50 rounded-lg">
                  <div>
                    <p className="text-sm font-medium text-gray-900">
                      Demande du {new Date(request.requestDate).toLocaleDateString('fr-FR')}
                    </p>
                    <p className="text-sm text-gray-500">
                      {request.startAt} - {request.endAt}
                    </p>
                  </div>
                  <StatusBadge status={request.status} />
                </div>
              ))}
            </div>
          ) : (
            <p className="text-gray-500 text-center py-4">
              Aucune demande trouvée
            </p>
          )}
        </div>
      </div>

      {/* Demandes en attente de validation */}
      <div className="bg-white shadow rounded-lg">
        <div className="px-6 py-4 border-b border-gray-200">
          <h2 className="text-lg font-medium text-gray-900">Demandes en attente de validation</h2>
        </div>
        <div className="p-6">
          {loadingPending ? (
            <LoadingSpinner />
          ) : pendingRequests && pendingRequests.length > 0 ? (
            <div className="space-y-4">
              {pendingRequests.slice(0, 5).map((request) => (
                <div key={request.requestID} className="flex items-center justify-between p-4 bg-gray-50 rounded-lg">
                  <div>
                    <p className="text-sm font-medium text-gray-900">
                      Demande du {new Date(request.requestDate).toLocaleDateString('fr-FR')}
                    </p>
                    <p className="text-sm text-gray-500">
                      Employé ID: {request.employeeID}
                    </p>
                  </div>
                  <div className="flex space-x-2">
                    <button className="px-3 py-1 bg-green-600 text-white text-xs rounded hover:bg-green-700">
                      Approuver
                    </button>
                    <button className="px-3 py-1 bg-red-600 text-white text-xs rounded hover:bg-red-700">
                      Rejeter
                    </button>
                  </div>
                </div>
              ))}
            </div>
          ) : (
            <p className="text-gray-500 text-center py-4">
              Aucune demande en attente
            </p>
          )}
        </div>
      </div>
    </div>
  );
};

export default Dashboard;